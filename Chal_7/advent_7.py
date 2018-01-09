"""
URL for challenge: http://adventofcode.com/2017/day/7
"""

from tinydb import TinyDB, Query

db = TinyDB('db.json')
program = {'name': '', 'weight': 0, 'parent': '', 'children': []}

def build_db():
    f = open("advent_7_input.txt")
    print("Building db...")
    # each line denotes one program
    for line in f.readlines():
        fields = obtain_parts(line)
        program['name'] = fields[0]
        program['weight'] = int(fields[1])
        program['children'] = fields[2]
        db.insert(program)
    f.close()


def part1():
    prog_query = Query()
    # making a custom query to get those
    # programs which have children
    parent_progs = db.search(prog_query.children.test(has_children))
    print("Updating children data...")
    # updating the 'parent' field
    # of all the children
    for prog in parent_progs:
        children = prog['children']
        for child_name in children:
            db.update({'parent': prog['name']}, prog_query.name == child_name)

    # the bottom program will be the
    # one whose 'parent' field is empty
    bottom_prog = db.get(prog_query.parent == '')
    print(bottom_prog)


def has_children(children):
    """
    used in the custrom query to
    check if a program has children
    """
    # if list is not empty
    # it returns true
    return bool(children)


def obtain_parts(line):
    """
    get the name, weight and
    children from the line
    """
    arrow = ' -> '
    # remove '\n' and split
    # the name and weight from
    # 'children' (if they exist)
    parts = line.strip().split(arrow)
    name_weight = parts[0].split()
    name = name_weight[0]
    weight = name_weight[1][1:-1]
    children = []
    if arrow in line:
        children = parts[1].split(', ')

    fields = [name, weight, children]
    return fields


def purge():
    """
    erase everything in the database
    """
    db.purge()


def part2():
    # making a query object
    prog_query = Query()
    # updating each of the 'programs'
    # with a field 'visited', set
    # to False in the beginning
    db.update({'visited': False})
    # adding another field 'bal_wt' (balancing
    # weight) to all the programs which have
    # children. this will hold the value of
    # the combined weight of the children
    #
    # after making the updates, a list of
    # affected ids is returned
    ids_updated = db.update({'bal_wt': 0}, prog_query.children.test(has_children))
    # parent_progs is a list of all
    # the parent programs. we use the
    # ids returned above to get the
    # parent programs from the db
    parent_progs = []
    for pid in ids_updated:
        parent_progs.append(db.get(doc_id=pid))

    print("Checking children...")
    for prog in parent_progs:
        result = check_prog_children(prog)
        # if the result is not an int, then it must
        # be a list. as soon as we get this, we can
        # break the loop since there is only one incorrect
        # weight and we need not look further
        if not isinstance(result, int):
            if not result[0]:
                break

    # only stores the children's names
    children = result[1]
    # stores all the data of the children
    children_data = []
    for child_name in children:
        children_data.append(db.get(prog_query.name == child_name))

    children_weight = []
    for child in children_data:
        children_weight.append(child['weight'])

    # sorting the weight list for the
    # computation below
    children_weight.sort()
    if children_weight[0] - children_weight[1] == 0:
        # this is for the case when the different weight
        # is larger. e.g. [3,3,3,3,4]
        # since the difference of the first two weights is
        # zero, that means they are the same and that implies
        # that the different weight must be at the end of the list
        weight_diff = children_weight[-1] - children_weight[0]
        outlier = children_weight[-1]

    else:
        # this case would be when the different weight is
        # smaller. e.g. [4,5,5,5,5,5]
        weight_diff = children_weight[1] - children_weight[0]
        outlier = children_weight[0]

    # we find the child which
    # had the different weight
    for child in children_data:
        if child['weight'] == outlier:
            different_child = child
            break

    # the weight that the different child should have is
    # its weight minus the weight of its children (bal_wt)
    # minus the weight_diff which was obtained above
    required_wt = different_child['weight'] - different_child['bal_wt'] - weight_diff
    print(different_child['name'], required_wt)

def check_prog_children(prog):
    """
    for each program, check
    the weight of its children. if
    their weights are imbalanced,
    then those are the children we
    are interested in

    1. children's weights are balanced -
            int showing their combined weight
            returned
    2. children's weights are not balanced -
            list returned: 'False' and list
            of children
    """
    prog_query = Query()
    # updating the visit status of
    # current program to True
    db.update({'visited': True}, prog_query.name == prog['name'])
    children = prog['children']
    # if the program doesn't have children,
    # then just return its own weight
    if not children:
        return prog['weight']

    # getting the first child's weight
    first_child = db.get(prog_query.name == children[0])
    if first_child['visited']:
        weight = first_child['weight']
    else:
        # if the child has not been visited yet,
        # recursively call the method on the child
        weight = check_prog_children(first_child)
        # if the return value is not an int(the weight),
        # then it must be the list of children where the
        # weights are off. return this value
        #
        # ********* IMPORTANT ***********
        # the next two lines are important since without
        # these, while returning from the statement
        #   'return (False, children)'
        # the list is lost as we return from the recursive
        # calls. the list of children gets modified and the
        # parents are returned instead of the children
        if not isinstance(weight, int):
            return weight

    # list to keep track of weights
    children_weight = [weight]
    for child_name in children[1:]:
        child = db.get(prog_query.name == child_name)
        if child['visited']:
            obtained_wt = child['weight']
        else:
            # same logic as for first child
            obtained_wt = check_prog_children(child)
            if not isinstance(obtained_wt, int):
                return obtained_wt

        # ******* KEY PART *********
        # if the weights don't match up, then this
        # is what we are looking for. we return the
        # current list of children
        if obtained_wt != weight:
            return (False, children)

        # if the weights are fine, append
        # them to the list
        children_weight.append(obtained_wt)

    bal_wt = sum(children_weight)
    prog_weight = prog['weight']
    # for the program, update the weight it is
    # balancing as the sum of its children's weights
    # and its own weight increases by the balanced weight
    db.update({'bal_wt': bal_wt, 'weight': prog_weight + bal_wt}, prog_query.name == prog['name'])
    # return the program's new weight
    return prog_weight + bal_wt


def run():
    chall = int(input("Please enter either 1 or 2 for the challenges: "))
    if chall == 1:
        part1()
    elif chall == 2:
        part2()
    else:
        print("You need to enter either 1 or 2")
        exit(1)


def test():
    """
    method to test out ideas
    and practice stuff
    """
    f = open("advent_7_input.txt")
    lines = f.readlines()[0:3]
    arrow = ' -> '
    for line in lines:
        parts = line.strip().split(arrow)
        name_weight = parts[0].split()
        name = name_weight[0]
        weight = name_weight[1][1:-1]
        if arrow in line:
            children = parts[1].split(', ')
            print(name, weight, children)
        else:
            print(name, weight)

    db.insert({"name": "John"})
    user_query = Query()
    result = db.contains(user_query.name == "John")
    print(result)

    l = [4, 5, 6, 23, 4]
    a, b, c, d, e = l
    print(c, e)
    if l:
        print("Yay")
    else:
        print("Noo")

    x = 5
    print(type(x))
    if isinstance(x, int):
        print("yay")
    else:
        print("noo")

purge()
build_db()
run()

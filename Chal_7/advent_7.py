from tinydb import TinyDB, Query
from pprint import pprint

db = TinyDB('/Users/AbhijayGupta/Projects/Advent_of_Code_2017/Chal_7/db.json')
program = {'name': '', 'weight': 0, 'parent': '', 'children': []}

def build_db():
    f = open("/Users/AbhijayGupta/Projects/Advent_of_Code_2017/Chal_7/advent_7_input.txt")
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
    if children:
        return True
    else:
        return False


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
    db.purge()


def part2():
    prog_query = Query()
    db.update({'visited': False})
    ids_updated = db.update({'bal_wt': 0}, prog_query.children.test(has_children))
    # parent_progs = db.search(prog_query.children.test(has_children))
    parent_progs = []
    for pid in ids_updated:
        parent_progs.append(db.get(doc_id=pid))

    print("Checking children...")
    for prog in parent_progs:
        result = check_prog_children(prog)
        # if the children's weights are
        # not balanced, print the children
        if not isinstance(result, int):
            if not result[0]:
                break

    children = result[1]
    print(children)
    children_data = []
    for child_name in children:
        children_data.append(db.get(prog_query.name == child_name))

    # print("all children")
    # pprint(children_data)
    children_weight = []
    for child in children_data:
        children_weight.append(child['weight'])

    print(children_weight)
    children_weight.sort()
    outlier = []
    weight_diff = 0
    if children_weight[0] - children_weight[1] == 0:
        weight_diff = children_weight[-1] - children_weight[0]
        outlier = [weight_diff, children_weight[-1]]
    else:
        weight_diff = children_weight[1] - children_weight[0]
        outlier = [weight_diff, children_weight[0]]

    for child in children_data:
        if child['weight'] == outlier[1]:
            annoying_child = child
            break

    required_wt = annoying_child['weight'] - annoying_child['bal_wt'] - outlier[0]
    print(annoying_child['name'], required_wt)

def check_prog_children(prog):
    prog_query = Query()
    db.update({'visited': True}, prog_query.name == prog['name'])
    # pprint(prog)
    children = prog['children']
    # if the program doesn't have
    # children, then do nothing
    if not children:
        return prog['weight']

    # getting the first child's weight
    first_child = db.get(prog_query.name == children[0])
    if first_child['visited']:
        weight = first_child['weight']
    else:
        weight = check_prog_children(first_child)
        if not isinstance(weight, int):
            return weight

    children_weight = [weight]
    for child_name in children[1:]:
        child = db.get(prog_query.name == child_name)
        if child['visited']:
            obtained_wt = child['weight']
        else:
            obtained_wt = check_prog_children(child)
            if not isinstance(obtained_wt, int):
                return obtained_wt

        if obtained_wt != weight:
            return (False, children)

        children_weight.append(obtained_wt)

    bal_wt = sum(children_weight)
    prog_weight = prog['weight']
    db.update({'bal_wt': bal_wt, 'weight': prog_weight + bal_wt}, prog_query.name == prog['name'])
    # print(db.get(prog_query.name == prog['name']))
    # print(prog['name'], prog_weight + bal_wt)
    # print()
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
    # f = open("advent_7_input.txt")
    # lines = f.readlines()[0:3]
    # arrow = ' -> '
    # for line in lines:
    #     parts = line.strip().split(arrow)
    #     name_weight = parts[0].split()
    #     name = name_weight[0]
    #     weight = name_weight[1][1:-1]
    #     if arrow in line:
    #         children = parts[1].split(', ')
    #         print(name, weight, children)
    #     else:
    #         print(name, weight)

    # db.insert({"name": "John"})
    # user_query = Query()
    # result = db.contains(user_query.name == "John")
    # print(result)

    # l = [4, 5, 6, 23, 4]
    # a, b, c, d, e = l
    # print(c, e)
    # if l:
    #     print("Yay")
    # else:
    #     print("Noo")

    x = 5
    print(type(x))
    if isinstance(x, int):
        print("yay")
    else:
        print("noo")

purge()
build_db()
run()
# test()

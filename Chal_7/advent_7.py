from tinydb import TinyDB, Query

db = TinyDB('db.json')
program = {'name': '', 'weight': 0, 'parent': '', 'children': []}

def build_db():
    f = open("advent_7_input.txt")
    print("Building db...")
    # each line denotes one program
    for line in f.readlines():
        fields = obtain_parts(line)
        program['name'], program['weight'], program['children'] = fields
        db.insert(program)


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

purge()
build_db()
run()

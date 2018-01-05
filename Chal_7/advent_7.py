from tinydb import TinyDB, Query

db = TinyDB('db.json')
program = {'name': '', 'weight': 0, 'parent': '', 'children': []}

def main():
    f = open("advent_7_input.txt")
    # each line denotes one program
    for line in f.readlines():
        fields = obtain_parts(line)
        name, weight, children = fields
        program['name'] = name
        program['weight'] = weight
        program['children'] = children

        prog_query = Query()
        prog_exists = db.contains(prog_query.name == name)
        if not prog_exists:
            db.insert(program)
            # if this program has children
            if children:
                program['parent'] = name
                for child in children:
                    program['name'] = child
                    db.insert(program)



def obtain_parts(line):
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

    l = [4, 5, 6, 23, 4]
    a, b, c, d, e = l
    print(c, e)
    if l:
        print("Yay")
    else:
        print("Noo")

test()
# run()

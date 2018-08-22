"""
URL for challenge: https://adventofcode.com/2017/day/12
"""

from tinydb import TinyDB, Query

db = TinyDB('db.json')

def main():
    f = open("/Users/AbhijayGupta/Projects/Advent_of_Code_2017/Chal_12/advent_12_input.txt")
    prog = {'prog': 0, 'conns': set(), 'visited': False}
    for l in f.readlines():
        line = l.replace(' ', '').strip().split('<->')
        prog_no = int(line[0])
        connections = line[1].split(',')
        # the numbers are stored as strings in the list
        # so we map them to integers and convert the
        # map object to a list
        conns = list(map(int, connections))
        prog['prog'] = prog_no
        prog['conns'] = conns
        db.insert(prog)


def part1():
    group_progid_0 = {0}
    query_obj = Query()
    prog0 = db.get(query_obj.prog == 0)
    group_progid_0.update(prog0['conns'])
    db.update({'visited': True}, query_obj.prog == 0)
    group_progid_0 = find_progs(db.all(), group_progid_0)
    print(group_progid_0)
    print(len(group_progid_0))

def find_progs(progs, group_progid_0):
    query_obj = Query()
    for prog in progs:
        if not prog['visited']:
            do_intersect = bool(group_progid_0.intersection(prog['conns']))
            if do_intersect:
                group_progid_0.add(prog['prog'])
                db.update({'visited': True}, query_obj.prog == prog['prog'])
                for conn in prog['conns']:
                    conn = db.get(query_obj.prog == conn)
                    find_progs([conn], group_progid_0)

    return group_progid_0


    # group_progid_0 = {0}
    # group_progid_0.update(prog_conn[0])
    # for key in prog_conn.keys():
    #     key_conns = set(prog_conn[key])
    #     do_intersect = bool(group_progid_0.intersection(key_conns))
    #     if do_intersect:
    #         group_progid_0.add(key)
    #         group_progid_0.update(key_conns)

    # print(group_progid_0)
    # print(len(group_progid_0))

    # group_progid_0 = set()
    # root = Node(0)
    # for conn in prog_conn[0]:
    #     root.insert(conn)


def run():
    # chall = int(input("Please enter either 1 or 2 for the challenges: "))
    chall = 1
    if chall == 1:
        part1()
    elif chall == 2:
        part2()
    else:
        print("You need to enter either 1 or 2")
        exit(1)

def purge_db():
    db.purge()

def test():
    # s = "454, 528, 621, 1023, 1199"
    # print(s.replace(' ', ''))
    a = {1, 2, 3}
    b = {4, 7, 6}
    # print(bool(a.intersection(b)))
    c = list(a.union(b))
    # for elem in c:
    #     c.append(random.randint(11,20))
    #     print(elem)

    print(db.all())

# test()
purge_db()
main()
run()

import random
"""
URL for challenge: https://adventofcode.com/2017/day/12
"""

def main():
    f = open("/Users/AbhijayGupta/Projects/Advent_of_Code_2017/Chal_12/advent_12_input.txt")
    prog_conn = {}
    for l in f.readlines():
        line = l.replace(' ', '').strip().split('<->')
        prog = int(line[0])
        connections = line[1].split(',')
        # the numbers are stored as strings in the list
        # so we map them to integers and convert the
        # map object to a list
        conns = list(map(int, connections))
        prog_conn[prog] = conns

    return prog_conn


def part1(prog_conn):
    group_progid_0 = {0}
    group_progid_0.update(prog_conn[0])
    for key in prog_conn.keys():
        key_conns = set(prog_conn[key])
        do_intersect = bool(group_progid_0.intersection(key_conns))
        if do_intersect:
            group_progid_0.add(key)
            group_progid_0.update(key_conns)

    print(group_progid_0)
    print(len(group_progid_0))


def run():
    chall = int(input("Please enter either 1 or 2 for the challenges: "))
    prog_conn = main()
    if chall == 1:
        part1(prog_conn)
    elif chall == 2:
        part2()
    else:
        print("You need to enter either 1 or 2")
        exit(1)


def test():
    # s = "454, 528, 621, 1023, 1199"
    # print(s.replace(' ', ''))
    a = {1, 2, 3}
    b = {4, 7, 6}
    # print(bool(a.intersection(b)))
    c = list(a.union(b))
    for elem in c:
        c.append(random.randint(11,20))
        print(elem)


test()
# main()
# run()

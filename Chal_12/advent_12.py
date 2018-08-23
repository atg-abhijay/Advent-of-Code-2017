"""
URL for challenge: https://adventofcode.com/2017/day/12
"""

def main():
    f = open("/Users/AbhijayGupta/Projects/Advent_of_Code_2017/Chal_12/advent_12_input.txt")
    programs = {}
    for l in f.readlines():
        line = l.replace(' ', '').strip().split('<->')
        prog_id = int(line[0])
        connections = line[1].split(',')
        # the numbers are stored as strings in the list
        # so we map them to integers and convert the
        # map object to a list
        conns = list(map(int, connections))
        # making a separate dictionary containing
        # the connections of a particular id and
        # the visit status of that id
        details = {}
        details["conns"] = conns
        details["visited"] = False
        # the program id will be the key
        # with the dict details as the value
        programs[prog_id] = details

    # print(programs)
    return programs


def part1(programs):
    # Adding program 0 and its connections
    # to the group and then setting
    # the visit status to True
    group_progid_0 = {0}
    prog0 = programs[0]
    group_progid_0.update(prog0['conns'])
    programs[0]['visited'] = True
    group_progid_0 = find_progs(programs.keys(), programs, group_progid_0)
    # print(group_progid_0)
    print("Programs linked to program ID 0:", len(group_progid_0))


def find_progs(keys, progs, group_progid_0):
    # check the visit status of each program and
    # if not visited, then proceed further.
    # if the connections of that program intersect
    # with the ids already in the group, then add
    # the id of that program to the group (update visit status)
    # and look at the connections themselves.
    # looking at the connections is a recursive step.
    # we save time by checking for visit status
    # at the beginning.
    for key in keys:
        details = progs[key]
        if not details['visited']:
            do_intersect = bool(group_progid_0.intersection(details['conns']))
            if do_intersect:
                group_progid_0.add(key)
                progs[key]['visited'] = True
                for conn in details['conns']:
                    # have to put 'conn' in a list since
                    # the loop looks at 'keys' which is an
                    # iterable instance. cannot give an int
                    find_progs([conn], progs, group_progid_0)

    return group_progid_0


def run():
    # chall = int(input("Please enter either 1 or 2 for the challenges: "))
    chall = 1
    programs = main()
    if chall == 1:
        part1(programs)
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
    # for elem in c:
    #     c.append(random.randint(11,20))
    #     print(elem)

# test()
# main()
run()

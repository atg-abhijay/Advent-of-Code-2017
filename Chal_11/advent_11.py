"""
URL for challenge: https://adventofcode.com/2017/day/11
"""

def main():
    f = open("advent_11_input.txt")
    data = f.readline()
    commands = data.split(',')
    """
    Consider the 6 directions as 6 vectors -
    v1 = i + j   (ne)    v4 = -i -j  (sw)
    v2 = 2j      (n)     v5 = i - j  (se)
    v3 = -i + j  (nw)    v6 = -2j    (s)

    v1 <-> v4, v2 <-> v6, v3 <-> v5
    They are inverses of each other. Therefore
    we can just use one of each of them. Also,
    v3 = v2 - v1. So, there are only 2 independent
    vectors here, v1 (ne) and v2 (n).

    If v were any vector in this hexagonal space, it
    can be expressed as -
            v = k1v1 + k2v2 + ... + k6v6
    for constants k1, k2, ... k6.
    Using the independence fact above,
            v = v1(k1 - k3 - k4 + k5) + v2 (k2 + k3 - k5 - k6)

    Constants and direction relation -
        k1 -> ne    k4 -> sw
        k2 -> n     k5 -> se
        k3 -> nw    k6 -> s

    """
    num_times = {'k1': 0, 'k2': 0, 'k3': 0, 'k4': 0, 'k5': 0, 'k6': 0}
    for command in commands:
        if command == 'n':
            num_times['k2'] += 1
        elif command == 'ne':
            num_times['k1'] += 1
        elif command == 'nw':
            num_times['k3'] += 1
        elif command == 's':
            num_times['k6'] += 1
        elif command == 'sw':
            num_times['k4'] += 1
        elif command == 'se':
            num_times['k5'] += 1

    return num_times


def part1(num_times):
    """
    The position vector v at any time can be
    given by -
        v = v1(k1 - k3 - k4 + k5) + v2 (k2 + k3 - k5 - k6)

    Since v1 and v2 are independent vectors, the
    least number of steps required to get to v
    will be the sum of the coefficients of v1 and v2
        Sum = k1 + k2 - k4 - k6
    """
    total_steps = num_times['k1'] + num_times['k2'] - num_times['k4'] - num_times['k6']
    print("Total steps required:", total_steps)

def part2():
    pass


def run():
    chall = int(input("Please enter either 1 or 2 for the challenges: "))
    num_times = main()
    if chall == 1:
        part1(num_times)
    elif chall == 2:
        part2()
    else:
        print("You need to enter either 1 or 2")
        exit(1)

def test():
    a = (2, 3)
    b = (-1, 4)
    # print(a+b)

    print(min(5,-4,2))

# test()
# main()
run()

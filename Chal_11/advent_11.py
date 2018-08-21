"""
URL for challenge: https://adventofcode.com/2017/day/11
"""

def main():
    f = open("advent_11_input.txt")
    data = f.readline()
    commands = data.split(',')
    # north is opposite to south
    # north-east is oppposite to south-west
    # north-west is oppposite to south-east
    # therefore only one variable needed for
    # each of the pairs.
    num_times = {'n': 0, 'ne': 0, 'nw': 0}
    for command in commands:
        if command == 'n':
            num_times['n'] += 1
        elif command == 'ne':
            num_times['ne'] += 1
        elif command == 'nw':
            num_times['nw'] += 1
        elif command == 's':
            num_times['n'] -= 1
        elif command == 'sw':
            num_times['ne'] -= 1
        elif command == 'se':
            num_times['nw'] -= 1

    return num_times


def part1(num_times):
    # using variables for ease of writing code
    n = num_times['n']
    ne = num_times['ne']
    nw = num_times['nw']
    # if ne and nw are both positive
    # or both negative, then their values
    # combine to contribute to north

    # if one of them is positive and the other
    # is negative, then we can leave the values
    # as is because there exists three unique
    # directions of movement in the grid
    if ne*nw > 0:
        if abs(ne) < abs(nw):
            n += ne
            nw -= ne
            ne = 0
        else:
            n += nw
            ne -= nw
            nw = 0

        num_times['n'] = n
        num_times['ne'] = ne
        num_times['nw'] = nw

    # irrespective of being positive or negative,
    # the sum of the absolute values of the steps
    # in the three directions is the total no. of steps
    total_steps = abs(n)+abs(ne)+abs(nw)
    print(num_times)
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

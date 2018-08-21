"""
URL for challenge: https://adventofcode.com/2017/day/11
"""

def main():
    f = open("advent_11_input.txt")
    data = f.readline()
    commands = data.split(',')
    commands_dict = {
        'n': (0, 2),
        'ne': (1, 1),
        'se': (1, -1),
        's': (0, -2),
        'sw': (-1, -1),
        'nw': (-1, 1)
    }
    num_times = {'n': 0, 'ne': 0, 'se': 0, 's': 0, 'sw': 0, 'nw': 0}
    for command in commands:
        if command == 'n':
            num_times['n'] += 1
        elif command == 'ne':
            num_times['ne'] += 1
        elif command == 'se':
            num_times['se'] += 1
        elif command == 's':
            num_times['s'] += 1
        elif command == 'sw':
            num_times['sw'] += 1
        elif command == 'nw':
            num_times['nw'] += 1
    print(num_times)


def part1(num_times):
    num_times['n'] -= num_times['s']
    num_times['ne'] -= num_times['sw']
    num_times['se'] -= num_times['nw']

    if abs(num_times['n']) > abs(num_times['se']):
        num_times['ne'] += num_times['se']
        num_times['n'] -= num_times['se']
        num_times['se'] = 0
        if num_times['n'] < 0:
            num_times['s'] = abs(num_times['n'])
            num_times['n'] = 0
        if num_times['ne'] < 0:
            num_times['sw'] = abs(num_times['ne'])
            num_times['ne'] = 0

    else:
        num_times['ne'] += num_times['n']
        num_times['se'] -= num_times['n']
        num_times['n'] = 0


def part2():
    pass


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
    a = (2, 3)
    b = (-1, 4)
    # print(a+b)

    print(min(5,-4,2))

test()
# main()

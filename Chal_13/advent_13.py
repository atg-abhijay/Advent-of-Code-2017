"""
URL for challenge: https://adventofcode.com/2017/day/13
"""

def main():
    f = open("advent_13_input.txt")
    depth_range = {}
    for l in f.readlines():
        line = l.replace(' ', '').strip()
        line_parts = line.split(':')
        depth = int(line_parts[0])
        scn_range = int(line_parts[1])
        depth_range[depth] = scn_range

    # print(depth_range)
    return depth_range


def run():
    chall = int(input("Please enter either 1 or 2 for the challenges: "))
    if chall == 1:
        part1()
    elif chall == 2:
        part2()
    else:
        print("You need to enter either 1 or 2")
        exit(1)


main()
# run()

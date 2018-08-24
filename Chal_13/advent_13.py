"""
URL for challenge: https://adventofcode.com/2017/day/13
"""
from pprint import pprint

def main():
    f = open("advent_13_input.txt")
    depth_range = {}
    scn_pos = 0
    for l in f.readlines():
        line = l.replace(' ', '').strip()
        line_parts = line.split(':')
        depth = int(line_parts[0])
        scn_range = int(line_parts[1])
        details = {}
        details['range'] = scn_range
        details['scn_pos'] = scn_pos
        details['scn_dirn'] = 1
        depth_range[depth] = details

    # pprint(depth_range)
    return depth_range


def part1(depth_range):
    packet_pos = -1
    depths_caught_at = []
    num_layers = sorted(depth_range.keys())[-1]
    for i in range(num_layers + 1):
        packet_pos += 1
        if packet_pos in depth_range:
            if depth_range[packet_pos]['scn_pos'] == 0:
                depths_caught_at.append(packet_pos)
        for key in depth_range.keys():
            layer = depth_range[key]
            if layer['scn_pos'] == 0:
                depth_range[key]['scn_dirn'] = 1
            elif layer['scn_pos'] == layer['range'] - 1:
                depth_range[key]['scn_dirn'] = -1

            depth_range[key]['scn_pos'] += depth_range[key]['scn_dirn']

    print(depths_caught_at)
    severity = 0
    for depth in depths_caught_at:
        severity += depth * depth_range[depth]['range']

    print("Severity:", severity)

def part2():
    pass


def run():
    chall = int(input("Please enter either 1 or 2 for the challenges: "))
    depth_range = main()
    if chall == 1:
        part1(depth_range)
    elif chall == 2:
        part2()
    else:
        print("You need to enter either 1 or 2")
        exit(1)


# main()
run()

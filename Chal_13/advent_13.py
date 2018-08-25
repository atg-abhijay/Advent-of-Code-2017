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
    # make the initial position
    # -1 since the first layer
    # is at depth 0
    packet_pos = -1
    # a list to hold the depths
    # at which we were caught
    depths_caught_at = []
    # layers do not exist at all the
    # depths. so we cannot use the number of
    # keys as the number of layers. the last
    # depth will tell us how many 'layers'
    # are there. we don't need to sort for
    # this question but it is for the case
    # if the input was jumbled up.
    num_layers = sorted(depth_range.keys())[-1]
    # without the '+1' the last layer would get skipped.
    # we need as many iterations as there are layers
    for i in range(num_layers + 1):
        packet_pos += 1
        # the packet will be located in a specific
        # layer. we check if that layer has a depth,
        # range or if it is a blank layer. if it is
        # a blank layer, there is nothing to do.
        if packet_pos in depth_range:
            # if the layer does have a depth, range -
            # we check if the scanner in that layer
            # is at the top of the layer. if it is,
            # we are caught and we add that packet
            # position (or depth) to the list of
            # where we were caught at.
            if depth_range[packet_pos]['scn_pos'] == 0:
                depths_caught_at.append(packet_pos)
        # loop for moving the positions of the
        # scanners.
        for key in depth_range.keys():
            layer = depth_range[key]
            # if the scanner is at the top,
            # it will be moving down and we
            # set the direction to '1' for down.
            if layer['scn_pos'] == 0:
                depth_range[key]['scn_dirn'] = 1
            # if the scanner is at the bottom,
            # it has to go up. so we change the
            # direction to '-1' for up.
            elif layer['scn_pos'] == layer['range'] - 1:
                depth_range[key]['scn_dirn'] = -1

            # the scanner gets moved according to
            # the direction decided upon.
            depth_range[key]['scn_pos'] += depth_range[key]['scn_dirn']

    print(depths_caught_at)
    severity = 0
    # the severity is calculated by summing
    # the product of the depth and the range
    # of the layers we were caught at.
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

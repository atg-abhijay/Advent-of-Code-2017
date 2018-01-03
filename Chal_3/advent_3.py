import math

"""
URL for challenge: http://adventofcode.com/2017/day/3
"""

def part1():
    """
    The Manhattan Distance would be:

    sum of (l-1), where l is the layer number
    in which the puzzle input lies,
    and the deviation of the puzzle input
    from the closest middle point among the
    4 middle points of the 4 sides of the layer
    """

    # let counting of layers start from 1
    # i.e. the number '1' is in layer 1
    puzzle_input = 265149
    temp = (math.sqrt(puzzle_input) + 1)/2
    # puzzle input lies in this layer
    layer = math.ceil(temp)
    # the number of elements in any layer l:
    # L_num = [2(l+1)-1]^2 - [2l-1]^2 = 8(l-1)
    num_in_layer = 8*(layer-1)
    # last number of any layer l:
    # L_last = (2l-1)^2
    last_previous_layer = math.pow(2*(layer-1)-1, 2)
    # the midpoints of each of
    # the sides of the layer
    midpoints_of_layer = []
    num_each_side = num_in_layer/4
    max_deviation = num_each_side/2
    for i in range(4):
        # Midpoint of a side of the layer:
        # Sum of last number of previous layer,
        # half of number of elements in one side,
        # number of elements in one side multiplied
        # by side number: 0,1,2 or 3
        midpoint = last_previous_layer + num_each_side/2 + num_each_side*i
        midpoints_of_layer.append(midpoint)

    # the number of steps is the difference between
    # the current layer and the first layer
    # plus the deviation of the puzzle input
    # from the closest middle point
    num_steps = layer - 1
    for midpoint in midpoints_of_layer:
        deviation = math.fabs(puzzle_input - midpoint)
        if deviation <= max_deviation:
            num_steps += deviation

    print(int(num_steps))


def part2():


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
    for i in range(4):
        print(i)

run()

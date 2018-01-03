import math

"""
URL for challenge: http://adventofcode.com/2017/day/3
"""

puzzle_input = 265149
grid = dict()

def part1():
    """
    The Manhattan Distance would be:

    sum of (l-1), where l is the layer number
    in which the puzzle input lies,
    and the deviation of the puzzle input
    from the closest middle point among the
    4 middle points of the 4 sides of the layer

    completed in constant time
    """

    # let counting of layers start from 1
    # i.e. the number '1' is in layer 1
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
    """
    (0,0) is initialized to '1'.
    check all the neighbours of the
    point under consideration.

    couldn't really think of a
    better method. solution comes fast
    though.
    """
    grid[(0, 0)] = 1
    coordinates_value = 0
    layer = 1
    x = 0; y = 0
    done = False
    while not done:
        # print("Layer: ", layer)
        # go right one step
        layer += 1; x += 1
        grid[(x,y)] = check_neighbours((x,y))

        # go up to the boundary of layer
        for y_up in range(y+1, layer):
            coord = (x, y_up)
            coordinates_value = check_neighbours(coord)
            if coordinates_value > puzzle_input:
                return coordinates_value
        y = y_up

        # go left till the boundary of layer
        for x_left in range(x-1, -layer, -1):
            coord = (x_left, y)
            coordinates_value = check_neighbours(coord)
            if coordinates_value > puzzle_input:
                return coordinates_value
        x = x_left

        # go down till the boundary of layer
        for y_down in range(y-1, -layer, -1):
            coord = (x, y_down)
            coordinates_value = check_neighbours(coord)
            if coordinates_value > puzzle_input:
                return coordinates_value
        y = y_down

        # go right till the boundary of layer
        for x_right in range(x+1, layer):
            coord = (x_right, y)
            coordinates_value = check_neighbours(coord)
            if coordinates_value > puzzle_input:
                return coordinates_value
        x = x_right


def check_neighbours(coordinates):
    """
    checking existence of all neighbours
    of the point given by coordinates

    actually checking itself as well.
    but since it hasn't been initialized
    yet, it's not a problem
    """
    x_coord = coordinates[0]
    y_coord = coordinates[1]
    coordinates_value = 0
    for x_move in [-1, 0, 1]:
        x = x_coord + x_move
        for y_move in [-1, 0, 1]:
            y = y_coord + y_move
            try:
                value = grid[(x,y)]
                coordinates_value += value
            except KeyError:
                pass

    grid[coordinates] = coordinates_value
    # print(coordinates_value)
    return coordinates_value

def run():
    chall = int(input("Please enter either 1 or 2 for the challenges: "))
    if chall == 1:
        part1()
    elif chall == 2:
        result = part2()
        print(result)
    else:
        print("You need to enter either 1 or 2")
        exit(1)

def test():
    for i in range(-1,4):
        print(i)

    x = 5
    print(-x)

    # coord = (0, 3)
    # d = dict()
    # d[coord] = 4
    # print(d[(0, 3)])
    # try:
    #     print(d[(0, 2)])
    # except KeyError:
    #     print("sorry")


run()
# test()
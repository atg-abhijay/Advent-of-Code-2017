"""
URL for challenge: http://adventofcode.com/2017/day/6
"""

def main():
    f = open("advent_6_input.txt")
    input_line = f.readline()
    banks_strings = input_line.split('\t')
    banks = list(map(int, banks_strings))
    return banks

def part1(banks):
    # banks = [1, 2, 1, 0]
    num_banks = len(banks)
    num_cycles = 0
    # dictionary which keeps track
    # of configurations observed
    configs_observed = {}
    # adding the first configuration.
    # have to use a tuple since a
    # dictionary cannot have a
    # mutable object as a key
    first_banks_tuple = tuple(banks)
    configs_observed[first_banks_tuple] = True

    repeat_obtained = False
    while not repeat_obtained:
        num_cycles += 1
        # finding the maximum number of blocks
        # i.e. number of blocks to move
        blocks_to_move = max(banks)
        # using index() also takes care of the
        # fact that in case of a tie for max
        # value, the lower index should be picked
        # (since index() gives the first occurence
        # of that max value)
        max_index = banks.index(blocks_to_move)
        # emptying the bank at that index
        banks[max_index] = 0

        pointer = max_index
        while blocks_to_move > 0:
            pointer = (pointer + 1) % num_banks
            blocks_to_move -= 1
            banks[pointer] += 1

        banks_tuple = tuple(banks)
        if banks_tuple not in configs_observed:
            configs_observed[banks_tuple] = True
        else:
            repeat_obtained = True
            # printing the repeated config
            print(banks)

    print(num_cycles)


def part2(banks):
    # banks = [1, 2, 1, 0]
    num_banks = len(banks)
    num_cycles = 0
    configs_observed = {}
    first_banks_tuple = tuple(banks)
    # the value is the cycle number
    # at which we are currently
    configs_observed[first_banks_tuple] = num_cycles

    repeat_obtained = False
    num_cycles_loop = 0
    while not repeat_obtained:
        num_cycles += 1
        blocks_to_move = max(banks)
        max_index = banks.index(blocks_to_move)
        banks[max_index] = 0

        pointer = max_index
        while blocks_to_move > 0:
            pointer = (pointer + 1) % num_banks
            blocks_to_move -= 1
            banks[pointer] += 1

        banks_tuple = tuple(banks)
        if banks_tuple not in configs_observed:
            configs_observed[banks_tuple] = num_cycles
        else:
            repeat_obtained = True
            print(banks)
            # number of cycles in the loop will be
            # the current number of cycles minus the
            # number of cycles when this config
            # occured previously
            num_cycles_loop = num_cycles - configs_observed[banks_tuple]

    print(num_cycles_loop)

def run():
    chall = int(input("Please enter either 1 or 2 for the challenges: "))
    banks = main()
    if chall == 1:
        part1(banks)
    elif chall == 2:
        part2(banks)
    else:
        print("You need to enter either 1 or 2")
        exit(1)

def test():
    l1 = [1, 2, 3, 4, 25, 5, 7, 9, 25]
    l2 = [1, 2, 3, 4, 25, 6, 5, 7, 9, 25]
    t1 = (4, 5, 2, 245, 2134)
    print(len(t1))
    print(t1[4])
    # d = {l1: False, l2: True}
    # print(d[tuple(l2)])
    # print(l1 >= l2)
    # m = max(l)
    # index = l.index(m)
    # print(m, index)

# test()
# main()
run()

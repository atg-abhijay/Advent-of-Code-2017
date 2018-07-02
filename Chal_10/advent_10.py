"""
URL for challenge: http://adventofcode.com/2017/day/10
"""

def main():
    f = open("advent_10_input.txt")
    input_data = f.readline()
    # print(input_data)
    lengths = input_data.split(',')
    # the lengths are currently stored as strings
    # we map them to ints and convert the map to a list
    lengths = list(map(int, lengths))
    # print(lengths)
    return lengths


def part1(lengths):
    circ_list = [x for x in range(256)]
    len_circ = len(circ_list)
    # print(circ_list)
    current_pos = 0
    skip_size = 0
    for length in lengths:
        list_slice = []
        reverse_slice = []
        indices_changed = []
        # extracting elements based on given length
        for i in range(length):
            index = (current_pos + i) % len_circ
            indices_changed.append(index)
            # list_slice contains the elements to be reversed
            list_slice.append(circ_list[index])

        # forming the reversed list
        for element in reversed(list_slice):
            reverse_slice.append(element)

        for i in range(len(indices_changed)):
            index = indices_changed[i]
            # updating the circ_list with the reversed element
            circ_list[index] = reverse_slice[i]

        current_pos += length + skip_size
        current_pos = current_pos % len_circ
        skip_size += 1

    result = circ_list[0] * circ_list[1]
    # print(circ_list)
    print(result)


def part2():
    pass

def run():
    chall = int(input("Please enter either 1 or 2 for the challenges: "))
    lengths = main()
    if chall == 1:
        part1(lengths)
    elif chall == 2:
        part2()
    else:
        print("You need to enter either 1 or 2")
        exit(1)


def test():
    # l = [x for x in range(256)]
    # print(l)
    # p = [4,6,2,7,1,8]
    # for elem in reversed(p):
    #     print(elem)
    # for i in range(1,6):
    #     print(i)

    x = 5
    y = 6
    var = 34
    var += (x + y)
    var = var % 16
    print(var)

# test()
# main()
run()

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


# have to pass other parameters as well since those
# are needed for part 2. for solely solving part 1,
# we only need the lengths
def part1(circ_list, lengths, current_pos, skip_size):
    len_circ = len(circ_list)
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
    # need the dictionary object for part 2
    d = dict()
    d['circ_list'] = circ_list
    d['current_pos'] = current_pos
    d['skip_size'] = skip_size
    d['result'] = result
    return d


def part2():
    f = open("advent_10_input.txt")
    suffix_list = [17, 31, 73, 47, 23]
    char_list = list(f.readline())
    lengths = []
    # convert each character into its ASCII code
    for char in char_list:
        lengths.append(ord(char))

    lengths += suffix_list
    circ_list = [x for x in range(256)]
    current_pos = 0
    skip_size = 0
    # have to perform 64 rounds
    for i in range(64):
        dic_obj = part1(circ_list, lengths, current_pos, skip_size)
        # the list, current_pos and skip_size are
        # to be preserved over the diff. iterations
        circ_list = dic_obj['circ_list']
        current_pos = dic_obj['current_pos']
        skip_size = dic_obj['skip_size']

    dense_hash = []
    position = 0
    for i in range(16):
        position = 16*i
        partial_result = 0
        # after taking XOR with 16 numbers, we
        # get the 'complete' partial_result. we
        # append that to the dense_hash
        for j in range(16):
            partial_result = partial_result ^ circ_list[position+j]
        dense_hash.append(partial_result)

    hex_list = []
    for num in dense_hash:
        # get the last two digits after
        # converting int to hex
        temp = hex(num)[-2:]
        hex_digits = ''
        # we need a leading zero if an
        # 'x' is present
        if temp[0] == 'x':
            hex_digits = '0' + temp[1]
        else:
            hex_digits = temp

        hex_list.append(hex_digits)

    # efficient way of making a string rather than
    # repeatedly concatenating to a single string
    print(''.join(hex_list))


def run():
    chall = int(input("Please enter either 1 or 2 for the challenges: "))
    if chall == 1:
        lengths = main()
        circ_list = [x for x in range(256)]
        d = part1(circ_list, lengths, 0, 0)
        print(d['result'])
    elif chall == 2:
        part2()
    else:
        print("\nYou need to enter either 1 or 2")
        exit(1)


def test():
    # l = [x for x in range(256)]
    # print(l)
    # p = [4,6,2,7,1,8]
    # for elem in reversed(p):
    #     print(elem)
    # for i in range(1,6):
    #     print(i)

    # x = 5
    # y = 6
    # var = 34
    # var += (x + y)
    # var = var % 16
    # print(var)

    # p = 7
    # answer = hex(p)
    # answer = answer[-2:]
    # if answer[0] != 0:
    #     answer[0] = 0
    # print(answer)

    output = '3efbe78a8d82f29979031a4aa0b16a9d'
    answer = '3efbe78a8d82f29979031a4aa0b16a9d'
    print(output == answer)

# test()
# main()
run()

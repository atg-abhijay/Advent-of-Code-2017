"""
URL for challenge: http://adventofcode.com/2017/day/2
"""

def part1():
    """
    find the difference between the
    maximum and minimum number in each
    line and add it to checksum
    """
    f = open("advent_2_input.txt")
    checksum = 0
    for line in f.readlines():
        int_list = get_list(line)
        checksum += max(int_list) - min(int_list)

    print(checksum)

def part2():
    """
    in each line, find the only two numbers
    where one completely divides the other.
    this is the result from that line.

    add up the results from all the lines
    """
    f = open("advent_2_input.txt")
    sum_of_row_result = 0
    for line in f.readlines():
        int_list = get_list(line)
        length = len(int_list)
        # get a specific number in the line
        for first_index in range(length-1):
            division_result = check_for_each_num(int_list, first_index)
            if division_result != 0:
                break

        sum_of_row_result += division_result

    print(int(sum_of_row_result))

def check_for_each_num(int_list, first_index):
    """
    check divisibility of number at first_index
    with all numbers that lie after it in the list
    """
    length = len(int_list)
    first_num = int_list[first_index]
    division_result = 0
    for second_index in range(first_index+1, length):
        second_num = int_list[second_index]
        if first_num % second_num == 0:
            division_result = first_num/second_num
            break
        elif second_num % first_num == 0:
            division_result = second_num/first_num
            break
        else:
            pass

    return division_result

def get_list(line):
    """
    convert tab-separated numbers
    into a list of integers
    """
    # remove the ending '\n'
    line = line.rstrip()
    # split the line into a list
    # using tabs ('\t') as delimiters
    string_list = line.split('\t')
    # the above list obtained has the
    # numbers stored as strings. use map()
    # to map each of the elements of string_list
    # to an int. cast the map object to a list
    int_list = list(map(int, string_list))
    return int_list


def run():
    chall = int(input("Please enter either 1 or 2 for the challenges: "))
    if chall == 1:
        part1()
    elif chall == 2:
        part2()
    else:
        print("You need to enter either 1 or 2")
        exit(1)

# def test():
#     for i in range(1,2):
#         print(i)

run()

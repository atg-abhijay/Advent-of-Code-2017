"""
URL for challenge: http://adventofcode.com/2017/day/2
"""

def part1():
    f = open("advent_2_input.txt")
    checksum = 0
    for line in f.readlines():
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
        checksum += max(int_list) - min(int_list)

    print(checksum)

def run():
    chall = int(input("Please enter either 1 or 2 for the challenges: "))
    if chall == 1:
        part1()
    elif chall == 2:
        part2()
    else:
        print("You need to enter either 1 or 2")
        exit(1)

part1()
# run()

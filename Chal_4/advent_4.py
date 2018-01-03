"""
URL for challenge: http://adventofcode.com/2017/day/4
"""

def part1():
    """
    pick a word. compare it to
    words ahead of it in the list
    """
    f = open("advent_4_input.txt")
    valid_passphrases = 0
    for line in f.readlines():
        string_list = line.split()
        valid = True
        length = len(string_list)
        for i in range(length-1):
            first_word = string_list[i]
            for j in range(i+1, length):
                if first_word == string_list[j]:
                    valid = False
                    print(line)

        if valid:
            valid_passphrases += 1

    print(valid_passphrases)

def run():
    # chall = int(input("Please enter either 1 or 2 for the challenges: "))
    chall = 1
    if chall == 1:
        part1()
    elif chall == 2:
        part2()
    else:
        print("You need to enter either 1 or 2")
        exit(1)

run()

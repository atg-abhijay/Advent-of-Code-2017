from pprint import pprint

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
                second_word = string_list[j]
                if first_word == second_word:
                    valid = False
                    print(line)
                    break
            if not valid:
                break

        if valid:
            valid_passphrases += 1

    print(valid_passphrases)
    f.close()


def part2():
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
        # length = 2
        for i in range(length-1):
            first_word = string_list[i]
            first_word_list = sorted(list(first_word))
            for j in range(i+1, length):
                second_word = string_list[j]
                second_word_list = sorted(list(second_word))
                # print(first_word_list, second_word_list)
                if first_word_list == second_word_list:
                    valid = False
                    print(line)
                    break
            if not valid:
                break

        if valid:
            valid_passphrases += 1

    print(valid_passphrases)
    f.close()

def run():
    chall = int(input("Please enter either 1 or 2 for the challenges: "))
    # chall = 2
    if chall == 1:
        part1()
    elif chall == 2:
        part2()
    else:
        print("You need to enter either 1 or 2")
        exit(1)

def test():
    f = open("advent_4_input.txt")
    line_1 = f.readline()
    line_2 = f.readline()
    print(line_1)
    print(line_2)
    l1_w1 = line_1.split()[0]
    print(l1_w1)
    result = sorted(list(l1_w1))
    print(result)

# test()
run()

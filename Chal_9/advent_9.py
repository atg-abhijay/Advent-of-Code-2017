"""
URL for challenge: https://adventofcode.com/2017/day/9
"""
def part1():
    chall_input = open("advent_9_input.txt").read()
    # chall_input = '{{<!!>},{<!!>},{<!!>},{<!!>}}'
    score = 0
    gp_open = 0
    to_check = True
    prev_char = ''
    for char in chall_input:
        if prev_char == '!':
            prev_char = ''
            continue
        elif char == '{' and to_check:
            gp_open += 1
            score += gp_open
        elif char == '}' and to_check:
            gp_open -= 1
        elif char == '<':
            to_check = False
        elif char == '>':
            to_check = True
        prev_char = char

    print("Total score:", score)


def part2():
    pass

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

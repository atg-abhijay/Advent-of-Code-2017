"""
URL for challenge: https://adventofcode.com/2017/day/9
"""
def part1():
    # using readlines() instead of read() to test all test
    # cases at once, which are present on different lines
    chall_input = open("advent_9_input.txt").readlines()
    for l in chall_input:
        # strip the line of the newline character
        line = l.strip()
        # keep track of the total score
        score = 0
        # gp_open increases by 1 when we nest one more level
        # and decreases by 1 when we come out of one level
        gp_open = 0
        # 'to_check' helps decide whether or not to check for
        # '{' or '}'. When we have the '<' denoting the start
        # of garbage, 'to_check' turns False. It only turns back
        # to True once we close the garbage i.e. we get to a '>'
        to_check = True
        # 'prev_char' keeps track of the previous character. When
        # the prev. char. is a '!', we have to negate the character
        # that follows it. So, we need to keep track of the prev. char.
        prev_char = ''
        for char in line:
            # we skip the current iteration if the prev. char. was a '!'.
            # Also, we change 'prev_char' to '' (blank) since we have skipped
            # the current character and we kind of start with a blank slate
            if prev_char == '!':
                prev_char = ''
                continue
            # 'to_check' has to be True. We don't go into the loop if we are in
            # the garbage currently. 'gp_open' increases since we have nested
            # deeper and the score increases by the level at which we are at
            # i.e. 'gp_open'
            elif char == '{' and to_check:
                gp_open += 1
                score += gp_open
            # come out 1 layer and therefore 'gp_open' decreases
            elif char == '}' and to_check:
                gp_open -= 1
            # garbage is starting and 'to_check' is made False
            elif char == '<':
                to_check = False
            # only if the garbage comes to an end does 'to_check' become True
            elif char == '>':
                to_check = True
            prev_char = char

        # print(line, "- Total score:", score)
        print("Total score:", score)


def part2():
    chall_input = open("advent_9_input.txt").readlines()
    for l in chall_input:
        line = l.strip()
        # stores the answer
        valid_gbg = 0
        inside_gbg = False
        prev_char = ''
        for char in line:
            # skip the current iteration if the previous
            # character was a '!'
            if prev_char == '!':
                prev_char = ''
                continue
            # we are at the beginning of garbage
            elif char == '<' and not inside_gbg:
                inside_gbg = True
            # we are at the end of garbage
            elif char == '>':
                inside_gbg = False
            # this also takes care of '<' WITHIN the garbage
            elif inside_gbg and char != '!':
                valid_gbg += 1
            prev_char = char

        # print(line, "- Total valid garbage:", valid_gbg)
        print("Total valid garbage:", valid_gbg)


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

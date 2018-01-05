"""
URL for challenge: http://adventofcode.com/2017/day/5
"""

def main():
    f = open("advent_5_input.txt")
    all_numbers_strings = f.readlines()
    for x in range(len(all_numbers_strings)):
        all_numbers_strings[x] = all_numbers_strings[x].rstrip()

    all_numbers = list(map(int, all_numbers_strings))
    f.close()
    return all_numbers

def part1(all_numbers):
    length = len(all_numbers)
    num_steps = 0
    curr_pos = 0 # current position
    while curr_pos < length:
        # getting the distance to move
        dist_to_move = all_numbers[curr_pos]
        # updating the offset by 1
        all_numbers[curr_pos] += 1
        # moving the pointer
        curr_pos += dist_to_move
        num_steps += 1

    print(num_steps)

def part2(all_numbers):
    length = len(all_numbers)
    num_steps = 0
    curr_pos = 0 # current position
    print("Calculating...")
    while curr_pos < length:
        # getting the distance to move
        dist_to_move = all_numbers[curr_pos]
        # updating the offset
        if dist_to_move >=3:
            all_numbers[curr_pos] -= 1
        else:
            all_numbers[curr_pos] += 1
        # moving the pointer
        curr_pos += dist_to_move
        num_steps += 1

    print(num_steps)

def run():
    chall = int(input("Please enter either 1 or 2 for the challenges: "))
    all_numbers = main()
    if chall == 1:
        part1(all_numbers)
    elif chall == 2:
        part2(all_numbers)
    else:
        print("You need to enter either 1 or 2")
        exit(1)

def test():
    l = [1, 2, 3, 4, 5, 6]
    for num in l:
        num = num+1
        print(num)
    print(l)

# test()
run()

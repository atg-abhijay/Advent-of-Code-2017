def main():
    """
    URL for challenge: http://adventofcode.com/2017/day/1
    """
    f = open("advent_1_input.txt")
    data = f.read()
    return data

def part1(data):
    sum_of_numbers = 0
    for i in range(len(data)-2):
        digit = int(data[i])
        next_digit = int(data[i+1])
        if digit == next_digit:
            sum_of_numbers += digit

    if data[-1] == data[0]:
        sum_of_numbers += int(data[-1])

    print(sum_of_numbers)

def part2(data):
    sum_of_numbers = 0
    length = len(data)
    offset = length/2
    for i in range(length):
        digit = int(data[i])
        index = int((i + offset) % length)
        next_digit = int(data[index])
        if digit == next_digit:
            sum_of_numbers += digit

    print(sum_of_numbers)

def run():
    chall = int(input("Please enter either 1 or 2 for the challenges: "))
    data = main()
    if chall == 1:
        part1(data)
    elif chall == 2:
        part2(data)
    else:
        print("You need to enter either 1 or 2")
        exit(1)

run()

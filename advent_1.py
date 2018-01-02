def main():
    """
    URL for challenge: http://adventofcode.com/2017/day/1
    """
    f = open("advent_1_input.txt")
    data = f.read()
    sum_of_numbers = 0
    for i in range(len(data)-2):
        digit = int(data[i])
        next_digit = int(data[i+1])
        if digit == next_digit:
            sum_of_numbers += digit

    if data[-1] == data[0]:
        sum_of_numbers += int(data[-1])

    print(sum_of_numbers)

main()

def main():
    f = open("advent_6_input.txt")
    input_line = f.readline()
    banks = input_line.split('\t')
    return banks

def part1(banks):
    pass

def run():
    chall = int(input("Please enter either 1 or 2 for the challenges: "))
    banks = main()
    if chall == 1:
        part1(banks)
    elif chall == 2:
        part2(banks)
    else:
        print("You need to enter either 1 or 2")
        exit(1)

main()
# run()

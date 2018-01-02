def main():
    """
    URL for challenge: http://adventofcode.com/2017/day/2
    """
    f = open("advent_2_input.txt")
    data = f.read()
    return data

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

main()
# run()

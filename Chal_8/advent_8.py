"""
URL for challenge: http://adventofcode.com/2017/day/8
"""
from tinydb import TinyDB, Query
from tinydb.operations import add, subtract

db = TinyDB('registers.json')

def main():
    f = open("advent_8_input.txt")
    register = {}
    print("Building db...")
    for line in f.readlines():
        line_list = line.split()
        register['name'] = line_list[0]
        register['command'] = line_list[1]
        register['amount'] = int(line_list[2])
        register['value'] = 0
        register['condition_reg'] = line_list[4]
        # print(line_list[4])
        register['inequality'] = line_list[5]
        register['condition_amount'] = int(line_list[6])
        db.insert(register)


def part1():
    reg_query = Query()
    print("Updating registers...")
    for register in db.all():
        status = evaluate_cond(register)
        if status:
            amount = register['amount']
            if register['command'] == 'inc':
                db.update(add('value', amount), reg_query.name == register['name'])
            else:
                db.update(subtract('value', amount), reg_query.name == register['name'])

    values = []
    for register in db.all():
        values.append(register['value'])

    max_value = max(values)
    # print(max_value)

    max_register = db.get(reg_query.value == max_value)
    print(max_register)


def part2():
    reg_query = Query()
    all_time_max = 0
    print("Updating registers...")
    for register in db.all():
        status = evaluate_cond(register)
        if status:
            amount = register['amount']
            # value = register['value']
            if register['command'] == 'inc':
                # new_value = value + amount
                db.update(add('value', amount), reg_query.name == register['name'])
            else:
                # new_value = value - amount
                db.update(subtract('value', amount), reg_query.name == register['name'])

            # db.update({'value': new_value}, reg_query.name == register['name'])
            new_value = db.get(reg_query.name == register['name'])['value']
            print(new_value)
            if all_time_max < new_value:
                all_time_max = new_value

    print("\nAll time max: ", all_time_max)

def evaluate_cond(register):
    reg_query = Query()
    cond_reg_name = register['condition_reg']
    # print(cond_reg_name)
    cond_reg_value = db.get(reg_query.name == cond_reg_name)['value']
    ineq = register['inequality']
    cond_amt = register['condition_amount']
    if ineq == '==':
        return cond_reg_value == cond_amt
    elif ineq == '!=':
        return cond_reg_value != cond_amt
    elif ineq == '>':
        return cond_reg_value > cond_amt
    elif ineq == '<':
        return cond_reg_value < cond_amt
    elif ineq == '>=':
        return cond_reg_value >= cond_amt
    elif ineq == '<=':
        return cond_reg_value <= cond_amt

def purge():
    db.purge()

def run():
    chall = int(input("Please enter either 1 or 2 for the challenges: "))
    # chall = 1
    main()
    if chall == 1:
        part1()
    elif chall == 2:
        part2()
    else:
        print("You need to enter either 1 or 2")
        exit(1)

def test():
    # f = open("advent_8_input.txt")
    # for line in f.readlines()[0:15]:
    #     print(line.split())
    db.purge()
    db.insert({'name': 'John', 'age': 22})
    print(db.all())
    # db.update(add('age', 5))
    # db.update(add('age', -3))
    # db.update(subtract('age', 5))
    db.update(subtract('age', -2))
    print(db.all())

purge()
# main()
# test()
run()

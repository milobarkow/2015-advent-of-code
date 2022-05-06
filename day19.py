import random
import re

def part1():
    distinct = []

    for move in data:
        for i in range(len(seed)):
            nextMove = ''
            if seed[i] == move[0].strip():
                nextMove = seed[:i] + move[1].strip() + seed[i + 1:]
            elif seed[i:i + 2] == move[0].strip():
                nextMove = seed[:i] + move[1].strip() + seed[i + 2:]

            if nextMove != '' and nextMove not in distinct:
                distinct.append(nextMove)

    print(len(distinct))
            

def part2():
    with open('input.txt') as file:
        data = [line.replace(' ', '').strip().split('=>') for line in file]

    seed = 'ORnPBPMgArCaCaCaSiThCaCaSiThCaCaPBSiRnFArRnFArCaCaSiThCaCaSiThCaCaCaCaCaCaSiRnFYFArSiRnMgArCaSiRnPTiTiBFYPBFArSiRnCaSiRnTiRnFArSiAlArPTiBPTiRnCaSiAlArCaPTiTiBPMgYFArPTiRnFArSiRnCaCaFArRnCaFArCaSiRnSiRnMgArFYCaSiRnMgArCaCaSiThPRnFArPBCaSiRnMgArCaCaSiThCaSiRnTiMgArFArSiThSiThCaCaSiRnMgArCaCaSiRnFArTiBPTiRnCaSiAlArCaPTiRnFArPBPBCaCaSiThCaPBSiThPRnFArSiThCaSiThCaSiThCaPTiBSiRnFYFArCaCaPRnFArPBCaCaPBSiRnTiRnFArCaPRnFArSiRnCaCaCaSiThCaRnCaFArYCaSiRnFArBCaCaCaSiThFArPBFArCaSiRnFArRnCaCaCaFArSiRnFArTiRnPMgArF'


    # count = 0
    # for line in data:
    #     count += len(line[0]) + len(line[1])

    # for line in data:
    #     first = line[0].replace('Rn', '(').replace('Ar', ')').replace('Y', ',')
    #     second = line[0].replace('Rn', '(').replace('Ar', ')').replace('Y', ',')

    #     for l in first:
    #         if l == '(' or l == ')':
    #             count -= 1
    #         elif l == ',':
    #             count -= 2

    #     for l in second:
    #         if l == '(' or l == ')':
    #             count -= 1
    #         elif l == ',':
    #             count -= 2



    # seed = seed.replace('Rn', '(')
    # seed = seed.replace('Ar', ')')
    # seed = seed.replace('Y', ',')

    # for c in seed:
    #     if c == '(' or c == ')':
    #         count -= 1
    #     elif c == ',':
    #         count -= 2
    


    # taken from the advent of code sub
    reps = data
    mol = seed

    target = mol
    part2 = 0

    while target != 'e':
        tmp = target
        for a, b in reps:
            if b not in target:
                continue

            target = target.replace(b, a, 1)
            part2 += 1

        if tmp == target:
            target = mol
            part2 = 0
            random.shuffle(reps)

    print(part2)

#207


   
    


part2()
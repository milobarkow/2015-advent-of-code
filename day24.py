from itertools import combinations


def part1():
    with open('input.txt') as file:
        data = [int(num.strip()) for num in file]

    #data = [1, 2, 3, 4, 5, 7, 8, 9, 10, 11]
    goal = sum(data) // 3

    checker = [0, 1000000]
    for i in range(len(data) // 2):
        print(i)
        combos = combinations(data, i)
        for combo in combos:
            if sum(combo) == goal:
                half = [num for num in data if num not in combo]
                for j in range(len(half)):
                    half_combos = combinations(half, j)
                    for half_combo in half_combos:
                        if sum(half_combo) == goal:
                            half_half = [num for num in half if num not in half_combo]
                            if len(combo) < len(half) and len(combo) < len(half_half):
                                first = combo
                            elif len(half) < len(combo) and len(half) < len(half_half):
                                first = half
                            else:
                                first = half_half

                            if len(first) < checker[1]:
                                checker[1] = len(first)

                                quant = 1
                                for num in first:
                                    quant *= num
                                checker[0] = quant
                            elif len(first) == checker[1]:
                                quant = 1
                                for num in first:
                                    quant *= num
                                if quant < checker[0]:
                                    checker[0] = quant
                                    checker[1] = len(first)
                            

    print(checker[0])


def part2():
    with open('input.txt') as file:
        data = [int(num.strip()) for num in file]

    #data = [1, 2, 3, 4, 5, 7, 8, 9, 10, 11]
    goal = sum(data) // 4

    checker = [0, 1000000]
    for i in range(len(data) // 2):
        print(i)
        combos = combinations(data, i)
        for combo in combos:
            if sum(combo) == goal:
                half = [num for num in data if num not in combo]
                for j in range(len(half)):
                    half_combos = combinations(half, j)
                    for half_combo in half_combos:
                        if sum(half_combo) == goal:
                            half_half = [num for num in half if num not in half_combo]
                            if len(combo) < len(half) and len(combo) < len(half_half):
                                first = combo
                            elif len(half) < len(combo) and len(half) < len(half_half):
                                first = half
                            else:
                                first = half_half

                            if len(first) < checker[1]:
                                checker[1] = len(first)

                                quant = 1
                                for num in first:
                                    quant *= num
                                checker[0] = quant
                            elif len(first) == checker[1]:
                                quant = 1
                                for num in first:
                                    quant *= num
                                if quant < checker[0]:
                                    checker[0] = quant
                                    checker[1] = len(first)
                            

    print(checker[0])

part2()

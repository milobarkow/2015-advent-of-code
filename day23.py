import math

def process_instruction(instruction, a, b):
    log = instruction[0]
    offset = 1
    if log == 'hlf':
        if instruction[1] == 'a':
            a = math.floor(a / 2)
        else:
            b = math.floor(b / 2)
    elif log == 'tpl':
        if instruction[1] == 'a':
            a *= 3
        else:
            b *= 3
    elif log == 'inc':
        if instruction[1] == 'a':
            a += 1
        else:
            b += 1
    elif log == 'jmp':
        offset = int(instruction[1])
    elif log == 'jie':
        if instruction[1][0] == 'a' and a % 2 == 0:
            offset = int(instruction[2])
        elif instruction[1][0] == 'b' and b % 2 == 0:
            offset = int(instruction[2])
    elif log == 'jio':
        if instruction[1][0] == 'a' and a == 1:
            offset = int(instruction[2])
        elif instruction[1][0] == 'b' and b == 1:
            offset = int(instruction[2])
    return a, b, offset



def part1():
    with open('input.txt') as file:
        data = [line.strip().split() for line in file]
    line_number, a, b = 0, 0, 0
    while line_number < len(data):
        instruction = data[line_number]
        a, b, offest = process_instruction(instruction, a, b)
        line_number += offest
    print(b)


def part2():
    with open('input.txt') as file:
        data = [line.strip().split() for line in file]
    line_number, a, b = 0, 1, 0
    while line_number < len(data):
        instruction = data[line_number]
        a, b, offest = process_instruction(instruction, a, b)
        line_number += offest
    print(b)

part2()
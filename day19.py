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

    bad_switches = {}
    for line in data:
        bad_switches[line[0]] = list([-1])


    #seed = 'ORnPBPMgArCaCaCaSiThCaCaSiThCaCaPBSiRnFArRnFArCaCaSiThCaCaSiThCaCaCaCaCaCaSiRnFYFArSiRnMgArCaSiRnPTiTiBFYPBFArSiRnCaSiRnTiRnFArSiAlArPTiBPTiRnCaSiAlArCaPTiTiBPMgYFArPTiRnFArSiRnCaCaFArRnCaFArCaSiRnSiRnMgArFYCaSiRnMgArCaCaSiThPRnFArPBCaSiRnMgArCaCaSiThCaSiRnTiMgArFArSiThSiThCaCaSiRnMgArCaCaSiRnFArTiBPTiRnCaSiAlArCaPTiRnFArPBPBCaCaSiThCaPBSiThPRnFArSiThCaSiThCaSiThCaPTiBSiRnFYFArCaCaPRnFArPBCaCaPBSiRnTiRnFArCaPRnFArSiRnCaCaCaSiThCaRnCaFArYCaSiRnFArBCaCaCaSiThFArPBFArCaSiRnFArRnCaCaCaFArSiRnFArTiRnPMgArF'
    seed = 'HOH'
    ret = step('e', seed, data, bad_switches, 0)
    print(ret)

    

def step(string, seed, data, bad_switches, count):
    if string == seed:
        return count
    else:
        new_string = ''
        for i in range(len(string)):
            checker_one = ''
            checker_two = ''
            if len(string) == 1:
                checker_one = string
            elif i < len(string) - 1:
                checker_one = string[i]
                checker_two = string[i : i + 2]
            else:
                checker_one = string[i]

            for line in data:
                if len(bad_switches[line[0]]) == 1:
                    if line[0] == checker_one:
                        new_string = string.replace(checker_one, line[1], 1)
                        if new_string == seed:
                            return count
                        elif new_string in seed and len(new_string) < len(string):
                            step(new_string, seed, data, bad_switches, count + 1)
                        else:
                            bad_switches[line[0]].append(string.index(line[0]))
                            step(new_string, seed, data, bad_switches, count)
                    elif checker_two != '' and line[0] == checker_two:
                        new_string = string.replace(checker_two, line[1], 1)
                        if new_string == seed:
                            return count
                        elif new_string in seed and len(new_string) < len(string):
                            step(new_string, seed, data, bad_switches, count + 1)
                        else:
                            bad_switches[line[0]].append(string.index(line[0]))
                            step(new_string, seed, data, bad_switches, count)
                else:
                    if line[0] == checker_one:
                        new_string = string[:bad_switches[line[0]][-1]] + string[bad_switches[line[0]][-1] + 1:].replace(checker_one, line[1], 1)
                        if new_string == seed:
                            return count
                        elif new_string in seed and len(new_string) < len(string):
                            step(new_string, seed, data, bad_switches, count + 1)
                        else:
                            if line[0] in string[bad_switches[line[0]][-1] + 1:]:
                                bad_switches[line[0]].append(string[bad_switches[line[0]][-1] + 1:].index(line[0]) + len(string[:bad_switches[line[0]][-1]]) -1)
                            step(new_string, seed, data, bad_switches, count)
                    elif checker_two != '' and line[0] == checker_two:
                        new_string = string[:bad_switches[line[0]][-1]] + string[bad_switches[line[0]][-1] + 1:].replace(checker_two, line[1], 1)
                        if new_string == seed:
                            return count
                        elif new_string in seed and len(new_string) < len(string):
                            step(new_string, seed, data, bad_switches, count + 1)
                        else:
                            if line[0] in string[bad_switches[line[0]][-1] + 1:]:
                                bad_switches[line[0]].append(string[bad_switches[line[0]][-1] + 1:].index(line[0]) + len(string[:bad_switches[line[0]][-1]]) - 1)
                            step(new_string, seed, data, bad_switches, count)

    return count

part2()
def part1():
    with open('input.txt') as file:
        data = [line.strip().split() for line in file]

    checker = {
        'children': 3,
        'cats': 7,
        'samoyeds': 2,
        'pomeranians': 3,
        'akitas': 0,
        'vizslas': 0,
        'goldfish': 5,
        'trees': 3,
        'cars': 2,
        'perfumes': 1
    }

    sues = []
    for line in data:
        newSue = {}
        newSue['rank'] = line[1][:-1]
        line = line[2:]

        for i in range(len(line) - 1):
            if line[i][-1:] == ':':
                val = line[i + 1].replace(',', '')
                newSue[line[i][:-1]] = int(val)

        sues.append(newSue)

    for sue in sues:
        good = True
        for key in sue:
            if key != 'rank' and sue[key] != checker[key]:
                good = False

        if good:
            print(sue['rank'])


def part2():
    with open('input.txt') as file:
        data = [line.strip().split() for line in file]

    checker = {
        'children': 3,
        'cats': 7,
        'samoyeds': 2,
        'pomeranians': 3,
        'akitas': 0,
        'vizslas': 0,
        'goldfish': 5,
        'trees': 3,
        'cars': 2,
        'perfumes': 1
    }

    sues = []
    for line in data:
        newSue = {}
        newSue['rank'] = line[1][:-1]
        line = line[2:]

        for i in range(len(line) - 1):
            if line[i][-1:] == ':':
                val = line[i + 1].replace(',', '')
                newSue[line[i][:-1]] = int(val)

        sues.append(newSue)

    for sue in sues:
        good = True
        for key in sue:
            if key != 'rank':
	            if key == 'cats' or key == 'trees':
	                if sue[key] <= checker[key]:
	                    good = False
	            elif key == 'pomeranians' or key == 'goldfish':
	                if sue[key] >= checker[key]:
	                    good = False
	            elif sue[key] != checker[key]:
	                good = False


        if good:
            print(sue['rank'])


part2()

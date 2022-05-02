from itertools import permutations

def part1():
	with open('input.txt') as file:
		data = [line.strip()[:-1].split(' ') for line in file]

	names = permutations(set([line[0] for line in data]))
	final_score = 0
	check_one = ""
	check_two = ""

	for line in names:
		score = 0
		for i in range(len(line)):
			if i == len(line) - 1:
				check_one = line[0]
				check_two = line[i - 1]
			elif i == 0:
				check_one = line[i + 1]
				check_two = line[-1]
			else:
				check_one = line[i + 1]
				check_two = line[i - 1]


			for entry in data:
				if line[i] == entry[0]:
					if check_one == entry[-1]:
						if 'lose' == entry[2]:
							score -= int(entry[3])
						else:
							score += int(entry[3])
					elif check_two == entry[-1]:
						if 'lose' == entry[2]:
							score -= int(entry[3])
						else:
							score += int(entry[3])
		final_score = max(final_score, score)
	print(final_score)


def part2():
	with open('input.txt') as file:
		data = [line.strip()[:-1].split(' ') for line in file]

	names = [line[0] for line in data] + ['empty']
	names = permutations(set(names))

	final_score = 0
	check_one = ""
	check_two = ""

	for line in names:
		score = 0
		for i in range(len(line)):
			if line[i] != 'empty':
				if i == len(line) - 1:
					check_one = line[0]
					check_two = line[i - 1]
				else:
					check_one = line[i + 1]
					check_two = line[i - 1]


				for entry in data:
					if line[i] == entry[0]:
						if check_one == entry[-1]:
							if 'lose' == entry[2]:
								score -= int(entry[3])
							else:
								score += int(entry[3])
						elif check_two == entry[-1]:
							if 'lose' == entry[2]:
								score -= int(entry[3])
							else:
								score += int(entry[3])
		final_score = max(final_score, score)
	print(final_score)


part2()
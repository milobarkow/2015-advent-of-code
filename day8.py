def part1():
	with open('input.txt') as file:
		data = [line.strip() for line in file]

	total = 0
	for line in data:
		total += len(line)
		line = line[1:-1].replace('\\\"', '?').replace('\\\\', '?').replace('\\x', '@')

		count = len(line) - (2 * line.count('@'))
		total -= count
	print(total)


def part2():
	with open('input.txt') as file:
		data = [line.strip() for line in file]

	total = 0
	for line in data:
		total += line.count('\"') + line.count('\\') + 2
	print(total)
		
part2()	

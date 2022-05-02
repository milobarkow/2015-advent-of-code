def part1():
	with open('input.txt') as file:
		data = [int(line.strip()) for line in file]

	count = 0
	for i in range(1 << len(data)):
		nextSet = [data[j] for j in range(len(data)) if (i & (1 << j))]
		if sum(nextSet) == 150:
			count += 1

	print(count)

def part2():
	with open('input.txt') as file:
		data = [int(line.strip()) for line in file]

	amount = len(data)
	for i in range(1 << len(data)):
		nextSet = [data[j] for j in range(len(data)) if (i & (1 << j))]
		if sum(nextSet) == 150:
			amount = min(amount, len(nextSet))

	print(amount)

part2()
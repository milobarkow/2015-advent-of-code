def part1():
	with open('input.txt') as file:
		data = [list(map(int, line.strip().split('x'))) for line in file]
	count = 0
	for line in data:
		x = line[0]
		y = line[1]
		z = line[2]
		small = min(x * y, y * z, x * z)
		ret = (2 * x * y) + (2 * y * z) + (2 * x * z)
		count += ret + small
	print(count)

def part2():
	with open('input.txt') as file:
		data = [list(map(int, line.strip().split('x'))) for line in file]

	count = 0
	for line in data:
		x = line[0]
		y = line[1]
		z = line[2]

		amount = (x + y + z - max(x, y, z)) * 2
		ret = x * y * z
		count += ret + amount
	print(count)

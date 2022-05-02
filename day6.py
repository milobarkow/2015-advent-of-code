def part1():
	with open('input.txt') as file:
		data = [line.strip() for line in file]

	grid = [[0 for i in range(1000)] for j in range(1000)]
	for line in data:
		line = line.split(',')
		line = [s.split(' ') for s in line]
		temp = []
		for t in line:
			for e in t:
				temp.append(e)
		if len(temp) == 7:
			x1 = int(temp[2])
			x2 = int(temp[5])
			y1 = int(temp[3])
			y2 = int(temp[6])
		else:
			x1 = int(temp[1])
			x2 = int(temp[4])
			y1 = int(temp[2])
			y2 = int(temp[5])
		for j in range(y1, y2 + 1):
			for i in range(x1, x2 + 1):
				if temp[1] == 'on':
					grid[j][i] = 1
				elif temp[1] == 'off':
					grid[j][i] = 0
				else:
					if grid[j][i] == 0:
						grid[j][i] = 1
					else:
						grid[j][i] = 0
	count = 0
	for i in range(1000):
		for j in range(1000):
			count += grid[i][j]

	print(count)


def part2():
	with open('input.txt') as file:
		data = [line.strip() for line in file]

	grid = [[0 for i in range(1000)] for j in range(1000)]
	for line in data:
		line = line.split(',')
		line = [s.split(' ') for s in line]
		temp = []
		for t in line:
			for e in t:
				temp.append(e)
		if len(temp) == 7:
			x1 = int(temp[2])
			x2 = int(temp[5])
			y1 = int(temp[3])
			y2 = int(temp[6])
		else:
			x1 = int(temp[1])
			x2 = int(temp[4])
			y1 = int(temp[2])
			y2 = int(temp[5])
		for j in range(y1, y2 + 1):
			for i in range(x1, x2 + 1):
				if temp[1] == 'on':
					grid[j][i] += 1
				elif temp[1] == 'off':
					if grid[j][i] > 0:
						grid[j][i] -= 1
				else:
					grid[j][i] += 2
	count = 0
	for i in range(1000):
		for j in range(1000):
			count += grid[i][j]

	print(count)

part2()
def part1():
	with open('input.txt') as file:
		data = [[x for x in line.strip()] for line in file]

	for i in range(100):
		copy = [[x for x in line] for line in data]
		for row in range(len(data)):
			for col in range(len(data[0])):
				if row == 0 and col == 0:
					lights = [copy[row + 1][col], copy[row + 1][col + 1], copy[row][col + 1]]
					amountOn = lights.count('#')
					if copy[row][col] == '#':
						if amountOn == 2 or amountOn == 3:
							pass
						else:
							data[row][col] = '.'
					else:
						if amountOn == 3:
							data[row][col] = '#'
				elif row == 0 and col == len(data) - 1:
					lights = [copy[row + 1][col], copy[row + 1][col - 1], copy[row][col - 1]]
					amountOn = lights.count('#')
					if copy[row][col] == '#':
						if amountOn == 2 or amountOn == 3:
							pass
						else:
							data[row][col] = '.'
					else:
						if amountOn == 3:
							data[row][col] = '#'
				elif row == len(data) - 1 and col == 0:
					lights = [copy[row - 1][col], copy[row - 1][col - 1], copy[row][col + 1]]
					amountOn = lights.count('#')
					if copy[row][col] == '#':
						if amountOn == 2 or amountOn == 3:
							pass
						else:
							data[row][col] = '.'
					else:
						if amountOn == 3:
							data[row][col] = '#'
				elif row == len(data) - 1 and col == len(data) - 1:
					lights = [copy[row - 1][col], copy[row - 1][col - 1], copy[row][col - 1]]
					amountOn = lights.count('#')
					if copy[row][col] == '#':
						if amountOn == 2 or amountOn == 3:
							pass
						else:
							data[row][col] = '.'
					else:
						if amountOn == 3:
							data[row][col] = '#'
				elif row == 0:
					lights = [copy[row][col - 1], copy[row][col + 1], copy[row + 1][col], copy[row + 1][col - 1], copy[row + 1][col + 1]]
					amountOn = lights.count('#')
					if copy[row][col] == '#':
						if amountOn == 2 or amountOn == 3:
							pass
						else:
							data[row][col] = '.'
					else:
						if amountOn == 3:
							data[row][col] = '#'
				elif row == len(data) - 1:
					lights = [copy[row][col - 1], copy[row][col + 1], copy[row - 1][col], copy[row - 1][col - 1], copy[row - 1][col + 1]]
					amountOn = lights.count('#')
					if copy[row][col] == '#':
						if amountOn == 2 or amountOn == 3:
							pass
						else:
							data[row][col] = '.'
					else:
						if amountOn == 3:
							data[row][col] = '#'
				elif col == 0:
					lights = [copy[row + 1][col], copy[row - 1][col], copy[row][col + 1], copy[row + 1][col + 1], copy[row - 1][col + 1]]
					amountOn = lights.count('#')
					if copy[row][col] == '#':
						if amountOn == 2 or amountOn == 3:
							pass
						else:
							data[row][col] = '.'
					else:
						if amountOn == 3:
							data[row][col] = '#'
				elif col == len(data) - 1:
					lights = [copy[row + 1][col], copy[row - 1][col], copy[row][col - 1], copy[row + 1][col - 1], copy[row - 1][col - 1]]
					amountOn = lights.count('#')
					if copy[row][col] == '#':
						if amountOn == 2 or amountOn == 3:
							pass
						else:
							data[row][col] = '.'
					else:
						if amountOn == 3:
							data[row][col] = '#'
				else:
					lights = [copy[row + 1][col], copy[row - 1][col], copy[row][col + 1], copy[row][col - 1], copy[row - 1][col - 1], copy[row - 1][col + 1], copy[row + 1][col - 1], copy[row + 1][col + 1]]
					amountOn = lights.count('#')
					if copy[row][col] == '#':
						if amountOn == 2 or amountOn == 3:
							pass
						else:
							data[row][col] = '.'
					else:
						if amountOn == 3:
							data[row][col] = '#'

	count = 0
	for line in data:
		count += line.count('#')

	print(count)




def part2():
	with open('input.txt') as file:
		data = [[x for x in line.strip()] for line in file]


	data[0][0] = '#'
	data[99][0] = '#'
	data[0][99] = '#'
	data[99][99] = '#'

	for i in range(100):
		copy = [[x for x in line] for line in data]
		for row in range(len(data)):
			for col in range(len(data[0])):
				if (row == 0 and col == 0) or (row == 0 and col == len(data) - 1) or (row == len(data) - 1 and col == 0) or (row == len(data) -1 and col == len(data) - 1):
					copy[row][col] = '#'
				elif row == 0:
					lights = [copy[row][col - 1], copy[row][col + 1], copy[row + 1][col], copy[row + 1][col - 1], copy[row + 1][col + 1]]
					amountOn = lights.count('#')
					if copy[row][col] == '#':
						if amountOn == 2 or amountOn == 3:
							pass
						else:
							data[row][col] = '.'
					else:
						if amountOn == 3:
							data[row][col] = '#'
				elif row == len(data) - 1:
					lights = [copy[row][col - 1], copy[row][col + 1], copy[row - 1][col], copy[row - 1][col - 1], copy[row - 1][col + 1]]
					amountOn = lights.count('#')
					if copy[row][col] == '#':
						if amountOn == 2 or amountOn == 3:
							pass
						else:
							data[row][col] = '.'
					else:
						if amountOn == 3:
							data[row][col] = '#'
				elif col == 0:
					lights = [copy[row + 1][col], copy[row - 1][col], copy[row][col + 1], copy[row + 1][col + 1], copy[row - 1][col + 1]]
					amountOn = lights.count('#')
					if copy[row][col] == '#':
						if amountOn == 2 or amountOn == 3:
							pass
						else:
							data[row][col] = '.'
					else:
						if amountOn == 3:
							data[row][col] = '#'
				elif col == len(data) - 1:
					lights = [copy[row + 1][col], copy[row - 1][col], copy[row][col - 1], copy[row + 1][col - 1], copy[row - 1][col - 1]]
					amountOn = lights.count('#')
					if copy[row][col] == '#':
						if amountOn == 2 or amountOn == 3:
							pass
						else:
							data[row][col] = '.'
					else:
						if amountOn == 3:
							data[row][col] = '#'
				else:
					lights = [copy[row + 1][col], copy[row - 1][col], copy[row][col + 1], copy[row][col - 1], copy[row - 1][col - 1], copy[row - 1][col + 1], copy[row + 1][col - 1], copy[row + 1][col + 1]]
					amountOn = lights.count('#')
					if copy[row][col] == '#':
						if amountOn == 2 or amountOn == 3:
							pass
						else:
							data[row][col] = '.'
					else:
						if amountOn == 3:
							data[row][col] = '#'

	count = 0
	for line in data:
		count += line.count('#')

	print(count)




part2()




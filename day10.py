def part1():
	data = '1113122113'

	for i in range(40):
		j = 0
		nextVal = ''
		temp = []
		while j < len(data):
			if len(temp) == 0:
				temp.append(data[j])
				j += 1
			elif data[j] == temp[0]:
				temp.append(data[j])
				j += 1
			else:
				nextVal += str(len(temp)) + temp[0]
				temp = []

		if len(temp) > 0:
			nextVal += str(len(temp)) + temp[0]

		data = nextVal 
	print(len(data))


def part2():
	data = '1113122113'

	for i in range(50):
		j = 0
		nextVal = ''
		temp = []
		while j < len(data):
			if len(temp) == 0:
				temp.append(data[j])
				j += 1
			elif data[j] == temp[0]:
				temp.append(data[j])
				j += 1
			else:
				nextVal += str(len(temp)) + temp[0]
				temp = []

		if len(temp) > 0:
			nextVal += str(len(temp)) + temp[0]

		data = nextVal 
	print(len(data))

part2()
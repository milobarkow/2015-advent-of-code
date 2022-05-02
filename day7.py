def part1():
	with open('input.txt') as file:
		data = [line.strip() for line in file]

	test = ['AND', 'OR', 'RSHIFT', 'LSHIFT', 'NOT']
	vals = {}

	for line in data:
		if len(line.strip().split(' ')) == 3 and line.strip().split(' ')[0].isnumeric():
			a = line.strip().split('->')[0].strip()
			b = line.strip().split('->')[1].strip()
			vals[b] = int(a)
		else:
			a = line.strip().split(' ')
			b = line.strip().split(' ')[-1]

			if a[0] == 'NOT':
				if a[1] not in vals:
					vals[a[1]] = -1
			elif a[1] == 'RSHIFT' or a[1] == 'LSHIFT':
				if a[0] not in vals:
					vals[a[0]] = -1
			else:
				if not a[0].isnumeric() and a[0] not in vals:
					vals[a[0]] = -1
				if not a[2].isnumeric() and a[2] not in vals:
					vals[a[2]] = -1

			if b not in vals:
				vals[b] = -1

	done = False
	while not done:
		for line in data:
			if len(line.strip().split(' ')) == 3 and not line.strip().split(' ')[0].isnumeric():
				a = line.strip().split('->')[0].strip()
				b = line.strip().split('->')[1].strip()
				vals[b] = vals[a]
			else:
				temp = line
				frontLine = line.split('->')[0].strip().split(' ')
				backLine = line.split('->')[1].strip()
				good = True
				if len(frontLine) > 1:
					if frontLine[0] == 'NOT':
						if vals[frontLine[1]] == -1:
							good = False
					elif frontLine[1] == 'LSHIFT' or frontLine[1] == 'RSHIFT':
						if vals[frontLine[0]] == -1:
							good = False
					else:
						if frontLine[0].isnumeric() == False and vals[frontLine[0]] == -1 or vals[frontLine[2]] == -1:
							good = False

				if good and len(frontLine) > 1:
					if 'AND' in temp:
						a = frontLine[0]
						b = frontLine[2]
						if a.isnumeric():
							a = int(a)
						else:
							a = int(vals[frontLine[0]])
						if b.isnumeric():
							b = int(b)
						else:
							b = int(vals[frontLine[2]])
						vals[backLine] = a & b
					elif 'OR' in temp:
						a = frontLine[0]
						b = frontLine[2]
						if a.isnumeric():
							a = int(a)
						else:
							a = int(vals[frontLine[0]])
						if b.isnumeric():
							b = int(b)
						else:
							b = int(vals[frontLine[2]])
						vals[backLine] = a | b
					elif 'LSHIFT' in temp:
						a = vals[frontLine[0]]
						b = frontLine[2]
						vals[backLine] = int(a) << int(b)
					elif 'RSHIFT' in temp:
						a = vals[frontLine[0]]
						b = frontLine[2]
						vals[backLine] = int(a) >> int(b)
					else:
						a = vals[frontLine[1]]
						vals[backLine] = int(a) ^ 65535
				
		done = True
		for item in vals.items():
			if item[1] == -1:
				done = False

	return vals['a']				


def part2():
	with open('input.txt') as file:
		data = [line.strip() for line in file]

	test = ['AND', 'OR', 'RSHIFT', 'LSHIFT', 'NOT']
	vals = {}
	newVal = part1()

	for line in data:
		if len(line.strip().split(' ')) == 3 and line.strip().split(' ')[0].isnumeric():
			a = line.strip().split('->')[0].strip()
			b = line.strip().split('->')[1].strip()
			vals[b] = int(a)
		else:
			a = line.strip().split(' ')
			b = line.strip().split(' ')[-1]

			if a[0] == 'NOT':
				if a[1] not in vals:
					vals[a[1]] = -1
			elif a[1] == 'RSHIFT' or a[1] == 'LSHIFT':
				if a[0] not in vals:
					vals[a[0]] = -1
			else:
				if not a[0].isnumeric() and a[0] not in vals:
					vals[a[0]] = -1
				if not a[2].isnumeric() and a[2] not in vals:
					vals[a[2]] = -1

			if b not in vals:
				vals[b] = -1

	vals['b'] = newVal
	done = False
	while not done:
		for line in data:
			if len(line.strip().split(' ')) == 3 and not line.strip().split(' ')[0].isnumeric():
				a = line.strip().split('->')[0].strip()
				b = line.strip().split('->')[1].strip()
				vals[b] = vals[a]
			else:
				temp = line
				frontLine = line.split('->')[0].strip().split(' ')
				backLine = line.split('->')[1].strip()
				good = True
				if len(frontLine) > 1:
					if frontLine[0] == 'NOT':
						if vals[frontLine[1]] == -1:
							good = False
					elif frontLine[1] == 'LSHIFT' or frontLine[1] == 'RSHIFT':
						if vals[frontLine[0]] == -1:
							good = False
					else:
						if frontLine[0].isnumeric() == False and vals[frontLine[0]] == -1 or vals[frontLine[2]] == -1:
							good = False

				if good and len(frontLine) > 1:
					if 'AND' in temp:
						a = frontLine[0]
						b = frontLine[2]
						if a.isnumeric():
							a = int(a)
						else:
							a = int(vals[frontLine[0]])
						if b.isnumeric():
							b = int(b)
						else:
							b = int(vals[frontLine[2]])
						vals[backLine] = a & b
					elif 'OR' in temp:
						a = frontLine[0]
						b = frontLine[2]
						if a.isnumeric():
							a = int(a)
						else:
							a = int(vals[frontLine[0]])
						if b.isnumeric():
							b = int(b)
						else:
							b = int(vals[frontLine[2]])
						vals[backLine] = a | b
					elif 'LSHIFT' in temp:
						a = vals[frontLine[0]]
						b = frontLine[2]
						vals[backLine] = int(a) << int(b)
					elif 'RSHIFT' in temp:
						a = vals[frontLine[0]]
						b = frontLine[2]
						vals[backLine] = int(a) >> int(b)
					else:
						a = vals[frontLine[1]]
						vals[backLine] = int(a) ^ 65535
				
		done = True
		for item in vals.items():
			if item[1] == -1:
				done = False

	print(vals['a'])




part2()



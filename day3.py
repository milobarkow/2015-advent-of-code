def part1():
	with open('input.txt') as file:
		data = file.readlines()[0]

	pos = [0, 0]
	cords = [[0, 0]]
	for e in data:
			if e == '^':
				pos[1] += 1
			elif e == 'v':
				pos[1] -= 1
			elif e == '>':
				pos[0] += 1
			else:
				pos[0] -= 1

		if pos not in cords:
			temp = [x for x in pos]
			cords.append(temp)
			
	print(len(cords))

def part2():
	with open('input.txt') as file:
		data = file.readlines()[0]

	pos1 = [0, 0]
	pos2 = [0, 0]
	cords = [[0, 0]]
	santa = True
	for e in data:
		if santa:
			if e == '^':
				pos1[1] += 1
			elif e == 'v':
				pos1[1] -= 1
			elif e == '>':
				pos1[0] += 1
			else:
				pos1[0] -= 1
		else:
			if e == '^':
				pos2[1] += 1
			elif e == 'v':
				pos2[1] -= 1
			elif e == '>':
				pos2[0] += 1
			else:
				pos2[0] -= 1
		santa = not santa
		if pos1 not in cords:
			temp = [x for x in pos1]
			cords.append(temp)

		if pos2 not in cords:
			temp = [x for x in pos2]
			cords.append(temp)
			
	print(len(cords))

part2()

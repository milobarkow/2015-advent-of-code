def part1():
	with open('input.txt') as file:
		data = file.readlines()[0]

	count = 0
	for e in data:
		if e == '(':
			count += 1
		elif e == ')':
			count -= 1

	print(count)

def part2():
	with open('input.txt') as file:
			data = file.readlines()[0]

	count = 0
	tracker = 1
	for e in data:
		if e == '(':
			count += 1
		elif e == ')':
			count -= 1
		if (count < 0):
			break
		else:
			tracker += 1

	print(tracker)

part2()

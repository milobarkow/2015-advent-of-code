import hashlib

def part1():
	key = 'iwrupvqb'
	i = 1
	found = False
	while not found:
		check = key + str(i)
		result = str(hashlib.md5(check.encode()).hexdigest())
		if result[:5] == '00000':
			found = True
		else:
			i += 1
	print(i)


def part2():
	key = 'iwrupvqb'
	i = 1
	found = False
	while not found:
		check = key + str(i)
		result = str(hashlib.md5(check.encode()).hexdigest())
		if result[:6] == '000000':
			found = True
		else:
			i += 1
		print(i)
	print(i)

part2()
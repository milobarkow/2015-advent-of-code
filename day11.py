def part1():
	passwordCheck = 'cqjxjnds'
	password = 'cqjxjnds'
	lets = 'abcdefghijklmnopqrstuvwxyz'

	done = False
	passed = False
	i = len(password) - 1
	while not done:
		three = False
		for j in range(len(password) - 3):
			if password[j: j + 3] == lets[lets.index(password[j]) : lets.index(password[j]) + 3]:
				three = True
				j = len(password)

		iou = False
		if 'i' in password or 'o' in password or 'l' in password:
			iou = True


		ones = False
		twos = False
		j = 0
		while j < len(password) - 1:
			if password[j] == password[j + 1] and not ones:
				ones = True
				j += 2
			elif password[j] == password[j + 1]:
				twos = True
				j = len(password)
			else:
				j += 1

		if three and not iou and twos:
			done = True
		else:
			if password[i] == 'z':
				password = password[:i] + 'a' + password[i + 1:]
				stepping = True
				j = i - 1
				while stepping:
					if password[j] == 'z':
						password = password[:j] + 'a' + password[j + 1:]
						j -= 1
					else:
						password = password[:j] + lets[lets.index(password[j]) + 1] + password[j + 1:]
						stepping = False
			else:
				password = password[:i] + lets[lets.index(password[i]) + 1] + password[i + 1:]

			print(password)

		if i < 0 and not done:
			i = len(password) - 1
	print(password)

def part2():
	passwordCheck = 'cqjxxzaa'
	password = 'cqjxxzaa'
	lets = 'abcdefghijklmnopqrstuvwxyz'

	done = False
	passed = False
	i = len(password) - 1
	while not done:
		three = False
		for j in range(len(password) - 3):
			if password[j: j + 3] == lets[lets.index(password[j]) : lets.index(password[j]) + 3]:
				three = True
				j = len(password)

		iou = False
		if 'i' in password or 'o' in password or 'l' in password:
			iou = True


		ones = False
		twos = False
		j = 0
		while j < len(password) - 1:
			if password[j] == password[j + 1] and not ones:
				ones = True
				j += 2
			elif password[j] == password[j + 1]:
				twos = True
				j = len(password)
			else:
				j += 1

		if three and not iou and twos:
			done = True
		else:
			if password[i] == 'z':
				password = password[:i] + 'a' + password[i + 1:]
				stepping = True
				j = i - 1
				while stepping:
					if password[j] == 'z':
						password = password[:j] + 'a' + password[j + 1:]
						j -= 1
					else:
						password = password[:j] + lets[lets.index(password[j]) + 1] + password[j + 1:]
						stepping = False
			else:
				password = password[:i] + lets[lets.index(password[i]) + 1] + password[i + 1:]

			print(password)

		if i < 0 and not done:
			i = len(password) - 1
	print(password)

part2()


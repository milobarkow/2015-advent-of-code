def part1():
	with open('input.txt') as file:
		data = [line.strip() for line in file]

	evil = ['ab', 'cd', 'pq', 'xy']
	vs = ['a', 'e', 'i', 'o', 'u']
	count = 0
	nice = False
	vowel = 0
	for word in data:
		nice = False
		vowel = 0
		for x in evil:
			if x in word:
				nice = True

		if not nice:
			nice = True
			for i in range(len(word) - 1):
					if word[i] == word[i + 1]:
						nice = False
			if not nice:			
				for let in word:
					if let in vs:
						vowel += 1
					
				if vowel >= 3:
					count += 1
	print(count)

def part2():
	with open('input.txt') as file:
		data = [line.strip() for line in file]

	nice = False
	count = 0
	for word in data:
		nice = False
		for i in range(len(word) - 2):
			if word[i] == word[i + 2]:
					nice = True

		if nice:
			nice = False
			for i in range(len(word) - 1):
				if not nice and word[i:i+2] in word[i + 2:]:
					nice = True
					count += 1


	print(count)

part2()

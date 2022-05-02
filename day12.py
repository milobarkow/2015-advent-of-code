import json
import re

def part1():
	with open('input.txt') as file:
		data = [re.split(' |,', line.strip()) for line in file]
		data = [[x for x in line if '-' in x or x.isnumeric()] for line in data]
		data = [int(line[0]) for line in data if line != []]
		ret = sum(data)
	print(ret)

def getFromObj(obj) -> int:
	count = 0
	if type(obj) == list:
		for x in obj:
			if type(x) == int or type(x) == str and '-' in x:
				count += int(x)
			else:
				count += getFromObj(x)
	elif type(obj) == dict:
		for key in obj:
			if key == 'red' or obj[key] == 'red':
				return 0		
		for key in obj:
			if type(obj[key]) == list or type(obj[key]) == dict:
				count += getFromObj(obj[key])
			else:
				if type(obj[key]) == int:
					count += int(obj[key])
	

	return count

def part2():
	with open('input.txt') as file:
		data = json.load(file)

	count = 0
	for x in data:
		count += getFromObj(x)

	print(count)

part2()


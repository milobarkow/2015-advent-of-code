def part1():
	with open('input.txt') as file:
		data = [line.strip().split() for line in file]

	ingreds = [{
		line[1]: int(line[2][:-1]),
		line[3]: int(line[4][:-1]),
		line[5]: int(line[6][:-1]),
		line[7]: int(line[8][:-1]),
		line[9]: int(line[10])
	} for line in data]
	score = 0

	for a in range(100):
		for b in range(100):
			for c in range(100):
				for d in range(100):
					if a + b + c + d == 100:
						cap = (a * ingreds[0]['capacity']) + (b * ingreds[1]['capacity']) + (c * ingreds[2]['capacity']) + (d * ingreds[3]['capacity'])
						dur = (a * ingreds[0]['durability']) + (b * ingreds[1]['durability']) + (c * ingreds[2]['durability']) + (d * ingreds[3]['durability'])
						fla = (a * ingreds[0]['flavor']) + (b * ingreds[1]['flavor']) + (c * ingreds[2]['flavor']) + (d * ingreds[3]['flavor'])
						tex = (a * ingreds[0]['texture']) + (b * ingreds[1]['texture']) + (c * ingreds[2]['texture']) + (d * ingreds[3]['texture'])
						cal = (a * ingreds[0]['calories']) + (b * ingreds[1]['calories']) + (c * ingreds[2]['calories']) + (d * ingreds[3]['calories'])

						if cal == 500 and cap > 0 and dur > 0 and fla > 0 and tex > 0:
							score = max(score, cap * dur * fla * tex)

	print(score)





part1()

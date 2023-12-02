from re import findall

with open('in.txt') as f:
	data = [line.strip() for line in f.readlines()]

count = 0

for i, line in enumerate(data):
	rounds = line.split(';')
	valid = True
	max_case = {'red': 0, 'green': 0, 'blue': 0}

	for round in rounds:
		round_info = findall(r'(\d+) (red|green|blue)', round)

		for inf in round_info:
			num, colour = inf
			num = int(num)
			max_case[colour] = max(max_case[colour], num)

	count += (max_case['red'] * max_case['green'] * max_case['blue'])
print(count)
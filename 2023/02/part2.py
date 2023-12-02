from re import findall

with open('in.txt') as f:
	data = [line.strip() for line in f.readlines()]

count = 0

for i, line in enumerate(data):
	rounds = line.split(';')
	valid = True
	max_case = [0, 0, 0]

	for round in rounds:
		round_info = findall(r'(\d+) (red|green|blue)', round)

		for inf in round_info:
			num, colour = inf
			num = int(num)

			if colour == 'green': max_case[0] = max(max_case[0], num)
			elif colour == 'blue': max_case[1] = max(max_case[1], num)
			elif colour == 'red': max_case[2] = max(max_case[2], num)
	count += (max_case[0] * max_case[1] * max_case[2])
print(count)
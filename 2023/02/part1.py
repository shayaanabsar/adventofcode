from re import findall

with open('in.txt') as f:
	data = [line.strip() for line in f.readlines()]

count = 0

for i, line in enumerate(data):
	rounds = line.split(';')
	valid = True

	for round in rounds:
		round_info = findall(r'(\d+) (red|green|blue)', round)

		for inf in round_info:
			num, colour = inf
			num = int(num)

			if colour == 'green' and num > 13: valid = False
			elif colour == 'blue' and num > 14 : valid = False
			elif colour == 'red' and num > 12: valid = False

		if not valid: break
	if valid: count += i+1

print(count)
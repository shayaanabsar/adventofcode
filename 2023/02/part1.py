from re import findall

with open('in.txt') as f:
	data = [line.strip() for line in f.readlines()]

allowed = {'red': 12, 'green': 13, 'blue': 14}
count = 0

for i, line in enumerate(data):
	rounds = line.split(';')
	valid = True

	for round in rounds:
		round_info = findall(r'(\d+) (red|green|blue)', round)

		for inf in round_info:
			num, colour = inf
			num = int(num)

			if num > allowed[colour]:
				valid = False
				break
			
		if not valid: break
	if valid: count += i+1

print(count)
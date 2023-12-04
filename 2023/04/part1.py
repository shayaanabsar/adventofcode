from re import finditer

with open('in.txt') as f: data = [line.strip() for line in f.readlines()]

score = 0

for line in data:
	line = line.split(':')[1]
	numbers, sep = [(i.start(), int(i.group())) for i in finditer(r'\d+', line)], line.index('|')
	
	winning_numbers     = {j for i, j in numbers if i < sep}
	scratchcard_numbers = {j for i, j in numbers if i > sep}

	matches = len(winning_numbers.intersection(scratchcard_numbers))

	if matches > 0: matches = 2 ** (matches - 1)
	score += matches

print(score)
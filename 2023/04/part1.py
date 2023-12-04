from re import finditer

with open('in.txt') as f: data = [line.strip() for line in f.readlines()]

score = 0

for line in data:
	line = line.split(':')[1]
	numbers, sep = finditer(r'\d+', line), line.index('|')
	
	winning_numbers, matches  = set(), 0

	for number in numbers:
		index, num = number.start(), int(number.group())

		if index < sep:
			winning_numbers.add(num)
		elif num in winning_numbers:
			matches += 1
	
	if matches > 0: matches = 2 ** (matches - 1)
	score += matches

print(score)
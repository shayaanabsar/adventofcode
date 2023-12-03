from re import finditer

with open('in.txt') as f: data = [line.strip() for line in f.readlines()]

max_x, max_y, sum = len(data[0]), len(data), 0

mapping = {}

for i, line in enumerate(data):
	numbers = finditer(r'\d+', line)

	for number in numbers:
		for j in range(number.start(), number.end()):
			mapping[(i, j)] = int(number.group())

for i, line in enumerate(data):
	for j, coord in enumerate(line):
		if coord != '*': continue

		parts = set()

		for y in (i-1, i, i+1):
			for x in (j-1, j, j+1):
				if (y, x) in mapping: parts.add(mapping[(y, x)])

		if len(parts) == 2:
			a, b = parts
			sum += a*b

print(sum)
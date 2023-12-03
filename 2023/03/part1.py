from re import finditer

with open('in.txt') as f: data = [line.strip() for line in f.readlines()]

max_x, max_y, sum = len(data[0]), len(data), 0

for i, line in enumerate(data):
	numbers = finditer(r'\d+', line)

	for number in numbers:
		start, end  = number.start(), number.end()

		for j in range(start, end):
			part = False

			for y in (i-1, i, i+1):
				for x in (j-1, j, j+1):
					if 0 <= y < max_y and 0 <= x < max_x:
						if not data[y][x].isdigit() and data[y][x] != '.':
							part = True
							break

			
			if part: break
		
		if part: 
			sum += int(number.group())

print(sum)
with open('in.txt') as f: data = [line.strip() for line in f.readlines()]

found = False

for i, line in enumerate(data):
	for j, c in enumerate(line):
		if c == '^':
			found = True
			break
	if found: break

start = (i, j)
ans = 0


for y, line in enumerate(data):
	for x, c in enumerate(line):
		if c == '#' or (y, x) == start: continue
		facing = 0
		i, j = start
		positions = {(i, j, facing)}
		while True:
			new_i, new_j = i, j

			if facing == 0: new_i -= 1
			elif facing == 1: new_j += 1
			elif facing == 2: new_i += 1
			elif facing == 3: new_j -= 1

			if not (0 <= new_i < len(data) and 0 <= new_j < len(data[0])):
				break

			if data[new_i][new_j] == '#' or (new_i, new_j) == (y, x):
				facing += 1
				facing %= 4
			else:
				i, j = new_i, new_j
				if (i, j, facing) in positions:
					ans += 1
					break
				positions.add((i, j, facing))

				
print(ans)

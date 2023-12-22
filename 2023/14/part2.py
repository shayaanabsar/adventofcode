with open('in.txt') as f: data = [list(line.strip()) for line in f.readlines()]
total = 0
N, W, S, E = 0, 1, 2, 3

def tilt(i, j, direction):
	global total

	curr_i, curr_j = i, j
	while True:
		new_i, new_j = curr_i, curr_j
		match direction:
			case 0: new_i -= 1
			case 2: new_i += 1
			case 3: new_j += 1
			case 1: new_j -= 1

		if new_i < 0 or new_i >= len(data) or new_j < 0 or new_j >= len(data[0]): break
		if data[new_i][new_j] != '.': break
		curr_i, curr_j = new_i, new_j
	
	data[i][j], data[curr_i][curr_j] = '.', 'O'
	total += (len(data) - curr_i)
	return (curr_i, curr_j)

total = 0

positions = []

for i, r in enumerate(data):
	for j, c in enumerate(r):
		if c == 'O': positions.append((i, j))

loads = []
patterns_seen = {}
pattern_length = 5
x = 0

for _ in range(1000):
	new_positions = []
	direction = x % 4
	if direction == N: positions = sorted(positions, key=lambda x: x[0])
	if direction == S: positions = sorted(positions, key=lambda x: x[0], reverse=True)
	if direction == W: positions = sorted(positions, key=lambda x: x[1])
	if direction == E: positions = sorted(positions, key=lambda x: x[1], reverse=True)
	total = 0
	for y, p in enumerate(positions): new_positions.append(tilt(p[0], p[1], x%4))
	x += 1
	positions = new_positions
	if x % 4 == 0:
		loads.append(total)
		currently_seen = len(loads)
		pattern = tuple(loads[currently_seen-pattern_length:currently_seen])
		if pattern in patterns_seen: break
		if currently_seen >= pattern_length: patterns_seen[pattern] = currently_seen

start, end = patterns_seen[pattern], x
pattern = loads[start:end]
idx = (1000000000 - start - 1) % len(pattern)
print(pattern[idx])
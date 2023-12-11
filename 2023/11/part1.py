with open('in.txt') as f: data = [list(line.strip()) for line in f.readlines()]

curr_y, curr_x = 0, 0

galaxies = []
columns = list(zip(*data))

count, j_offsets = 0, []

for c in columns:
	if '#' not in c: count += 1
	j_offsets.append(count)

i_offset = 0

for i, row in enumerate(data):
	for j, c in enumerate(row):
		if c == '#': 
			galaxies.append((i+i_offset, j+j_offsets[j]))
	if '#' not in row: i_offset += 1

seen = set()
sum = 0

for g1 in galaxies:
	for g2 in galaxies:
		if g1 != g2 and (g2, g1) not in seen:
			seen.add((g1, g2))
			sum += abs(g1[0] - g2[0]) + abs(g1[1] - g2[1])

print(sum)
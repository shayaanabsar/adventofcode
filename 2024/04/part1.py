from copy import copy

with open('in.txt') as f: data = [line.strip() for line in f.readlines()]

positions = []

dirs = [(-1, -1), (-1, 0), (-1, +1),
		(+0, -1), (+0, +1),
		(+1, -1), (+1, +0), (+1, +1)]

for i, col in enumerate(data):
	for j, l in enumerate(col):
		if l == 'X': positions.append((i, j, None))

for letter in 'MAS':
	new_positions = []
	for i, j, dir in positions:
		if dir is None:
			for n, d in enumerate(dirs):
				i_change, j_change = d
				if (0 <= i+i_change < len(data) ) and (0 <= j+j_change < len(data[0])) and data[i+i_change][j+j_change] == letter:
					new_positions.append((i+i_change, j+j_change, n))
				
		else:
			i_change, j_change = dirs[dir]
			if (0 <= i+i_change < len(data)) and (0 <= j+j_change < len(data[0])) and data[i+i_change][j+j_change] == letter:
				new_positions.append((i+i_change, j+j_change, dir))

	positions = copy(new_positions)

print(len(positions))
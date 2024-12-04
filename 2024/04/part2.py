with open('in.txt') as f: data = [line.strip() for line in f.readlines()]

positions = []

for i, col in enumerate(data):
	for j, l in enumerate(col):
		if l == 'A': positions.append((i, j))

diagonals = [
	[(-1, -1), (0, 0), (+1, +1)],
	[(-1, +1), (0, 0), (+1, -1)]
]

count = 0

for i, j in positions:
	strings = []
	for diagonal in diagonals:
		string = ''

		for i_change, j_change in diagonal:
			new_i, new_j = i+i_change, j+j_change

			if (0 <= new_i < len(data) ) and (0 <= new_j < len(data[0])):
				string += data[new_i][new_j]

		strings.append(string)
	
	if strings[0] in ('SAM', 'MAS') and strings[1] in ('SAM', 'MAS'): count += 1

print(count)
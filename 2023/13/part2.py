with open('in.txt') as f:
	data = [line.strip() for line in f.readlines()] + ['']
	grids, curr_grid = [], []

	for line in data:
		if line == '': 
			grids.append(curr_grid)
			curr_grid = []
		else: curr_grid.append(line)

def is_reflection(list, line):
	left_ptr, right_ptr = line, line+1
	differs = 0

	while True:
		if left_ptr < 0 or right_ptr > len(list) - 1: break
		if differs > 1: return False
		
		for i, v in enumerate(list[left_ptr]):
			if v != list[right_ptr][i]: differs += 1

		right_ptr += 1
		left_ptr  -= 1

	return differs == 1

count = 0

for grid in grids:
	columns = list(zip(*grid))

	for i, c in enumerate(columns[:-1]):
		if is_reflection(columns, i): count += (i + 1)

	for i, r in enumerate(grid[:-1]):
		if is_reflection(grid, i): count += (100 * (i + 1))

print(count)
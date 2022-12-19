with open('in.txt') as f:
	pattern = f.readline()

rocks = [
	'####',
	' # \n###\n # ',
	'  #\n  #\n###',
	'#\n#\n#\n#',
	'##\n##'
]

grid = set()

STOP = 0

def is_hitting(rock_pos):
	if rock_pos.intersection(grid) :
		return True
	
	for (i, j) in rock_pos:
		if i < -3:
			return True
		if j < 0 or j >= 7:
			return True
	return False

def move_down(rock_pos):
	new_rock_pos = {(i-1, j) for (i, j) in rock_pos}

	if not is_hitting(new_rock_pos):
		return new_rock_pos
	return STOP

def move_sideways(rock_pos, direction):
	if direction == '>':
		shift = 1
	else:
		shift = -1

	new_rock_pos = {(i, j+shift) for (i, j) in rock_pos}

	if not is_hitting(new_rock_pos):
		return new_rock_pos
	return rock_pos

highest = 0
direction_count = 0

for i in range(2023):
	rock = rocks[i % 5]
	rows = rock.split('\n')

	if i >= 1:
		highest = max(grid, key=lambda x:x[0])[0] + 4

	rock_pos = set()
	for y, row in enumerate(rows[::-1]):
		for x, char in enumerate(row):
			if char == '#':
				rock_pos.add((highest+y, x+2))

	
	if i == 0:
		highest = 0
	while True:
		rock_pos = move_sideways(rock_pos, pattern[direction_count % len(pattern)])	
		direction_count += 1
		test = move_down(rock_pos)

		if test == STOP:
			grid = grid.union(rock_pos)
			break
		else:
			rock_pos = test

from collections import defaultdict
from re import findall

with open('in.txt') as f:
	maze = [defaultdict(lambda: ' ') for _ in range(6)]
	data = f.readlines()
	text_maze = '\n'.join(data[:-1])

	dims = 50
	start = None

	for i, line in enumerate(data[:-1]):
		line = line.strip('\n')

		for j, char in enumerate(line):
			new_i, new_j = i, j

			if i // dims == 0:
				if j // dims == 1:
					face = 0
				else:
					face = 1
			elif i // dims == 1:
				face = 2
			elif i // dims == 2:
				if j // dims == 0:
					face = 3
				else:
					face = 4
			else:
				face = 5

			new_i, new_j = i % dims, j % dims

			if char != ' ': 
				maze[face][(new_i, new_j)] = char
			if i == 0 and start is None and char == '.': start = [new_i, new_j]


	instructions = findall(r'\d+[RL]', data[-1])
	instructions = [(int(i[:-1]), i[-1]) for i in instructions]

dims -= 1

wraparounds = {
	(0, 0): (5, 90), (0, 90): (1, 90), (0, 180): (2, 180), (0, 270): (3, 90),
	(1, 0): (5, 0), (1, 90): (4, 270), (1, 180): (2, 270), (1, 270): (0, 270),
	(2, 0): (0, 0), (2, 90): (1, 0), (2, 180): (4, 180), (2, 270): (3, 180),
	(3, 0): (2, 90), (3, 90): (4, 90), (3, 180): (5, 180), (3, 270): (0, 90),
	(4, 0): (2, 0), (4, 90): (1, 270), (4, 180): (5, 270), (4, 270): (3, 270),
	(5, 0): (3, 0), (5, 90): (4, 0), (5, 180): (1, 180), (5, 270): (0, 180)
} # Checked wraparounds and they are right

def handle_wraparound(bearing, face, pos):
	new_face, new_bearing = wraparounds[(face, bearing)]
	i, j = pos

	# Issue over

	if face == 0:
		if new_face == 5: i, j = j, 0
		elif new_face == 1: i, j = i, 0
		elif new_face == 2: i, j = 0, j
		elif new_face == 3: i, j = dims - i, 0
	elif face == 1:
		if new_face == 5: i, j = dims, j
		elif new_face == 4: i, j = dims - i, dims
		elif new_face == 2: i, j = j, dims
		elif new_face == 0: i, j = i, dims
	elif face  == 2:
		if new_face == 0: i, j = dims, j
		elif new_face == 1: i, j = dims, i
		elif new_face == 4: i, j = 0, j
		elif new_face == 3: i, j = 0, i
	elif face == 3:
		if new_face == 2: i, j = j, 0
		elif new_face == 4: i, j = i, 0
		elif new_face == 5: i, j = 0, j
		elif new_face == 0: i, j = dims-i, 0 
	elif face == 4:
		if new_face == 2: i, j = dims, j
		if new_face == 1: i, j = dims-i, dims
		if new_face == 5: i, j = j, dims
		if new_face == 3: i, j = i, dims
	elif face == 5:
		if new_face == 3: i, j = dims, j
		if new_face == 4: i, j = dims, i
		if new_face == 1: i, j = 0, j
		if new_face == 0: i, j = 0, i

	pos = (i, j)

	return pos, new_bearing, new_face


def move(bearing, face, pos):
	d_i, d_j = 0, 0

	match bearing:
		case 0:
			d_i = -1
		case 90:
			d_j = 1
		case 180:
			d_i = 1
		case 270:
			d_j = -1

	new_pos = (pos[0]+d_i, pos[1]+d_j)

	if maze[face][new_pos] == '.':
		return True, face, new_pos, bearing
	elif maze[face][new_pos] == '#':
		return False, face, pos, bearing
	else:
		new_pos, new_bearing, new_face = handle_wraparound(bearing, face, pos)

		if maze[new_face][new_pos] == '.':
			return True, new_face, new_pos, new_bearing
		elif maze[new_face][new_pos] == '#':
			return False, face, pos, bearing
		
face, pos, curr_bearing = 0, start, 90

for instruction in instructions:
	steps, direction = instruction

	for _ in range(steps):
		keep_going, face, pos, curr_bearing, = move(curr_bearing, face, pos)
		if not keep_going: break
	
	if direction == 'L':
		curr_bearing -= 90
	elif direction == 'R':
		curr_bearing += 90

	curr_bearing %= 360

match curr_bearing:
	case 90:
		f = 0
	case 180:
		f = 1
	case 270:
		f = 2
	case 0:
		f = 3

i, j = pos[0]+1, pos[1]+1

match face:
	case 0:
		j += 50
	case 1:
		j += 100
	case 2:
		i += 50
		j += 50
	case 3:
		i += 100
	case 4:
		i += 100
		j += 50
	case 5:
		i += 150

print(1000*i + 4*j + f)
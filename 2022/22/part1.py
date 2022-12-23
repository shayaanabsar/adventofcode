from collections import defaultdict
from re import findall

with open('in.txt') as f:
	maze = defaultdict(lambda: ' ')
	data = f.readlines()
	start = None
	
	for i, line in enumerate(data[:-1]):
		line = line.strip('\n')
		
		for j, char in enumerate(line):
			if char != ' ':
				maze[(i+1, j+1)] = char
				if (i == 0 and char == '.') and (start is None):
					start = (i+1, j+1)
		
	instructions = findall(r'\d+[RL]', data[-1])
	instructions = [(int(i[:-1]), i[-1]) for i in instructions]

def get_changes(curr_bearing):
	x_change, y_change = 0, 0

	if curr_bearing == 90:
		x_change = 1
	elif curr_bearing == 180:
		y_change = 1
	elif curr_bearing == 270:
		x_change = -1
	elif curr_bearing == 0:
		y_change = -1

	return (x_change, y_change)

def check_next(curr_pos, curr_bearing):
	curr_bearing += 180
	curr_bearing %= 360

	x_change, y_change = get_changes(curr_bearing)
	curr_y, curr_x = curr_pos

	while (maze[(curr_y+y_change, curr_x+x_change)]) != ' ':
		curr_x += x_change
		curr_y += y_change

	if maze[(curr_y, curr_x)] != '#':
		return (curr_y, curr_x)
	return False
	

def move(curr_pos, curr_bearing):
	x_change, y_change = 0, 0
	
	x_change, y_change = get_changes(curr_bearing)
	curr_y, curr_x = curr_pos

	match maze[(curr_y+y_change, curr_x+x_change)]:
		case ' ':
			return check_next(curr_pos, curr_bearing)
		case '#':
			return False
		case '.':
			return (curr_y+y_change, curr_x+x_change)


curr_bearing = 90
curr_pos = start

for (length, direction) in instructions:
	for i in range(length):
		test = move(curr_pos, curr_bearing)

		if test != False:
			curr_pos = test
		else:
			break

	if direction == 'L':
		curr_bearing -= 90
	else:
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

print((1000 * curr_pos[0]) + (4 * curr_pos[1] + f))
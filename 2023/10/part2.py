from collections import deque

with open('in.txt') as f: data = [list(line.strip()) for line in f.readlines()]

connections = {'|': {(1, 0), (-1, 0)}, '-': {(0, 1), (0, -1)}, 
			   'L': {(0, 1), (-1, 0)}, 'J': {(0, -1), (-1, 0)}, 
			   '7': {(1, 0), (0, -1)}, 'F': {(1, 0), (0, 1)}, '.': {}, 'S': {}}


new_maze = []
found = False

for i, col in enumerate(data):
	for j, row in enumerate(col):
		if data[i][j] == 'S':
			start = (i*2, j*2)
			conns = set()
			for y in (-1, 0, 1):
				for x in (-1, 0, 1):
					tmp_i, tmp_j = -y, -x
					if (-y, -x) in connections[data[i+y][j+x]]:
						conns.add((y, x))

			for sym in connections:
				if conns == connections[sym]:
					data[i][j] = sym
					break

			found = True
			break
	if found: break


for i in range(len(data)):
	new_row = []
	for j in range(len(data[i])):
		new_row.append(data[i][j])
		if (0, 1) in connections[data[i][j]]: new_row.append('-')
		else: 
			new_row.append('.')
	
	new_col = []
	for j in range(len(new_row)):
		if (1, 0) in connections[new_row[j]]: new_col.append('|')
		else: new_col.append('.')
	new_maze.append(new_row)
	new_maze.append(new_col)

height, width  =  len(new_maze), len(new_maze[0])

queue = deque([start])
cycle = {start}

while queue:
	y, x = queue.popleft()
	for del_y, del_x in connections[new_maze[y][x]]:
		new_y, new_x = y+del_y, x+del_x

		if (new_y, new_x) not in cycle:
			queue.append((new_y, new_x))
	cycle.add((y, x))

queue = deque()
dots  = set()
seen = set()

for i, row in enumerate(new_maze):
	for j, char in enumerate(row):
		if (i, j) not in cycle:
			new_maze[i][j] = '.'
		if new_maze[i][j] == '.': 
			dots.add((i, j))
			if i in (0, height-1) or j in (0, width-1): 
				queue.append((i, j))


while queue:
	current = queue.popleft()
	if current in seen: continue
	i, j = current

	for y in (i-1, i, i+1):
		for x in (j-1, j, j+1):
			if 0 <= y < height - 1 and 0 <= x < width - 1:
				if (y, x) not in cycle: queue.append((y, x))

	seen.add(current)

inside = dots.difference(seen)
truly_inside = set()

for i, j in inside:
	if i % 2 == j % 2 == 0: truly_inside.add((i, j))
print(len(truly_inside))
from collections import deque

with open('in.txt') as f: data = [list(line.strip()) for line in f.readlines()]

connections = {'|': {(1, 0), (-1, 0)}, '-': {(0, 1), (0, -1)}, 
			   'L': {(0, 1), (-1, 0)}, 'J': {(0, -1), (-1, 0)}, 
			   '7': {(1, 0), (0, -1)}, 'F': {(1, 0), (0, 1)}, '.': {}, 'S': {}}

found = False

for i, col in enumerate(data):
	for j, row in enumerate(col):
		if data[i][j] == 'S':
			start = (i, j)
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

queue = deque([(start, 0)])
seen = {start}
max_distance = float('-inf')

while queue:
	idx, distance = queue.popleft()
	y, x = idx
	for del_y, del_x in connections[data[y][x]]:
		new_y, new_x = y+del_y, x+del_x

		if (new_y, new_x) not in seen:
			queue.append(((new_y, new_x), distance+1))
	max_distance = max(max_distance, distance)
	seen.add((y, x))

print(max_distance)

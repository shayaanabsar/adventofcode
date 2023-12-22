from collections import deque

with open('in.txt') as f: data = [list(line.strip()) for line in f.readlines()]
height, width = len(data), len(data[0])

rotate = {(0, '\\'): 270, (90, '\\'): 180, (180, '\\'): 90, (270, '\\'): 0, (0, '/'): 90, (90, '/'): 0, (180, '/'): 270, (270, '/'): 180}

def move(i, j, b):
	ni, nj = i, j
	match b:
		case 0: ni -= 1
		case 90: nj += 1
		case 180: ni += 1
		case 270: nj -= 1
	return (ni, nj)

queue = deque([(0, 0, 90)])
seen_positions = set()
visited = {(0, 0)}

while queue:
	i, j, b = queue.popleft()
	
	if i < 0 or i > height-1 or j < 0 or j > width-1: continue
	if (i, j, b) in seen_positions: continue
	seen_positions.add((i, j, b))
	match data[i][j]:
		case '/': b = rotate[(b, '/')]
		case '\\':b = rotate[(b, '\\')]
		case '-':
			if b not in (90, 270): 
				queue.append((i, j, 90))
				queue.append((i, j, 270))
				continue
		case '|':
			if b not in (0, 180):
				queue.append((i, j, 0))
				queue.append((i, j, 180))
				continue
	visited.add((i, j))
	ni, nj = move(i, j, b)
	queue.append((ni, nj, b))

print(len(visited))
	
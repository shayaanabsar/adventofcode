from collections import deque

with open('in.txt') as f: map = [line.strip() for line in f.readlines()]

starting_positions = []

for i, r in enumerate(map):
	for j, c in enumerate(r):
		if c == '0':
			starting_positions.append((i, j))
			
t = 0

for s in starting_positions:
	queue = deque([s])
	nines_reached = 0

	while queue:
		i, j  = queue.popleft()
		level = int(map[i][j])

		if level == 9:
			t += 1
			continue

		possible_moves = [
			(i-1, j),
			(i, j-1), (i, j+1),
			(i+1, j)
		]

		for i, j in possible_moves:
			if 0 <= i < len(map) and 0 <= j < len(map[0]):
				if int(map[i][j]) == level + 1:
					queue.append((i, j))

print(t)
from collections import deque
from string import ascii_lowercase, ascii_uppercase

grid = []

with open('in.txt', 'r') as file:
	data = file.readlines()

	for line in data:
		grid.append(line.strip('\n'))

heights = ascii_lowercase

def get_neighbours(i, j):
	if grid[i][j] == 'E':
		 curr_height = 24
	elif grid[i][j] == 'S':
		curr_height = 0
	else:
		curr_height = heights.index(grid[i][j])

	poss_neighbours = [
		(i, j+1),
		(i, j-1),
		(i+1, j),
		(i-1, j)
	]

	actual_neighbours = []

	for neighbour in poss_neighbours:
		y, x = neighbour
		if 0 <= y < len(grid) and 0 <= x < len(grid[0]):
			if grid[y][x] == 'E':
				new_height = 25
			elif grid[y][x] == 'S':
				new_height = 0
			else:
				new_height = heights.index(grid[y][x])

			if new_height <= curr_height + 1:
				actual_neighbours.append(neighbour)

	return actual_neighbours

start = None
end = None

def djikstras(start):
	distances = {}

	for i in range(len(grid)):
		for j in range(len(grid[0])):
			if grid[i][j] == 'E':
				end = (i, j)

			if (i, j) == start:
				distances[(i, j)] = 0
			else:
				distances[(i, j)] = float('inf')

	explored = set()
	queue = deque()
	queue.append(start)

	while queue != deque():
		while True:
			curr = queue.popleft()

			if curr not in explored or len(queue) == 0:
				break

		for neighbour in get_neighbours(curr[0], curr[1]):
			i, j = neighbour
			distances[(i, j)] = min(distances[(i, j)], distances[curr] + 1)	
			queue.append((i, j))
		
		if curr == end:
			return distances[end]
		if curr in explored:
			return float('inf')

		explored.add(curr)
		queue = deque(sorted(queue, key=lambda x:distances[x]))

smallest = float('inf')

for i in range(len(grid)):
	for j in range(len(grid[0])):
		if grid[i][j] in 'Sa':
			smallest = min(smallest, djikstras((i, j)))
print(smallest)
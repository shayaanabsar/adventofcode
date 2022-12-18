from collections import deque
from functools import lru_cache

cubes = set()

x_dims = [float('inf'), float('-inf')]
y_dims = [float('inf'), float('-inf')]
z_dims = [float('inf'), float('-inf')]

with open('in.txt') as f:
	for line in f.readlines():
		x, y, z = tuple(int(i) for i in line.strip('\n').split(','))
		x_dims = [min(x_dims[0], x), max(x_dims[1], x)]
		y_dims = [min(y_dims[0], y), max(y_dims[1], y)]
		z_dims = [min(z_dims[0], z), max(z_dims[1], z)]
		cubes.add((x, y, z))

def get_neighbours(cube):
	x, y, z = cube

	return {
			(x, y, z-1),
			(x, y, z+1),
			(x, y-1, z),
			(x, y+1, z),
			(x-1, y, z),
			(x+1, y, z)
		}

def check_neighbours(cube):
	neighbours = get_neighbours(cube)

	open_faces = 0

	for neighbour in neighbours:
		if neighbour not in cubes and dfs(neighbour):
			open_faces += 1
	
	return open_faces

@lru_cache
def dfs(curr):
	global x_dims
	global y_dims
	global z_dims

	stack = [curr]
	seen = set()

	while stack:
		x, y, z = stack.pop()
		if (x, y, z) in seen or (x, y, z) in cubes:
			continue
		if (x < x_dims[0] or x > x_dims[1]) or (y < y_dims[0] or y > y_dims[1]) or (z < z_dims[0] or z > z_dims[1]):
			return True

		neighbours = get_neighbours((x, y, z))
		
		for neighbour in neighbours:
			if neighbour not in seen.union(cubes):
				stack.append(neighbour)
		seen.add((x, y, z))
		
	return False 

faces = 0


for cube in cubes:
	faces += check_neighbours(cube)
print(faces)
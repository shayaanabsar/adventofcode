cubes = set()

with open('in.txt') as f:
	for line in f.readlines():
		cubes.add(tuple(int(i) for i in line.strip('\n').split(',')))

def check_neighbours(cube):
	x, y, z = cube

	neighbours = {
		(x, y, z-1),
		(x, y, z+1),
		(x, y-1, z),
		(x, y+1, z),
		(x-1, y, z),
		(x+1, y, z)
	}

	open_faces = 6

	open_faces -= len(cubes.intersection(neighbours))
	
	return open_faces

faces = 0

for cube in cubes:
	faces += check_neighbours(cube)
print(faces)
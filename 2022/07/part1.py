with open('in.txt', 'r') as file:
	data = file.readlines()

curr_path = []
path_sizes = {}

in_ls = False

for line in data:
	line = line.strip('\n')

	if line[:4] == '$ cd':
		in_ls = False

		if '..' in line:
			curr_path.pop()
		else:
			curr_path.append(line[5:])
	if in_ls:
		if line [:3] != 'dir':
			size, file = line.split()
			for i in range(1, len(curr_path)+1):
				if tuple(curr_path[:i]) not in path_sizes:
					path_sizes[tuple(curr_path[:i])] = int(size)
				else:
					path_sizes[tuple(curr_path[:i])] += int(size)
	if line[:4] == '$ ls':
		in_ls = True

c = 0

for path in path_sizes:
	size = path_sizes[path]

	if size <= 100000:
		c += size
print(c)
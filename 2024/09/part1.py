from collections import deque

with open('in.txt') as f: diskmap = f.readline().strip()

free_space, file_space = deque([]), deque([])
id_number, count = 0, 0

for i, n in enumerate(diskmap):
	n = int(n)
	for j in range(n):
		if i % 2 == 0: 
			file_space.append(id_number)
		else:
			free_space.append(count)
			file_space.append(-1)
		count += 1
	if i % 2 == 0: id_number += 1

while free_space:
	file = file_space.pop()
	if file == -1: continue
	gap  = free_space.popleft()
	if gap >= len(file_space):
		file_space.append(file)
	else:
		file_space[gap] = file

s = 0
for i, f in enumerate(file_space):
	s += (i * f)
print(s)
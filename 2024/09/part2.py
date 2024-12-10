from copy import copy

with open('in.txt') as f: diskmap = f.readline().strip()

free_space, file_space = [], []
id_number, count = 0, 0

for i, n in enumerate(diskmap):
	n = int(n)

	if i % 2 == 1:
		free_space.append((count, n)) # start, length
	else:
		file_space.append((id_number, count, n )) # id, start, length
		if i % 2 == 0: id_number += 1

	
	count += n

for i, file in enumerate(copy(file_space[::-1])):
	i = id_number - i - 1
	file_id, file_start, file_length = file

	for j, gap in enumerate(free_space):
		gap_start, gap_length = gap

		if gap_length < file_length: continue
		if file_start < gap_start: break

		new_gap_length = gap_length - file_length
		new_gap_start  = gap_start  + file_length

		if new_gap_length > 0:
			free_space[j] = (new_gap_start, new_gap_length)
		else:
			free_space.remove(free_space[j])
		
		file_space[i] = ((file_id, gap_start, file_length))
		break

s = 0
for f in file_space:
	file_id, file_start, file_length = f

	for n in range(file_start, file_start+file_length):
		s += file_id * n

print(s)
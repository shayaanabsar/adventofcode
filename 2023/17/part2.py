from heapq import heappush, heappop

with open('in.txt') as f: data = [line.strip() for line in f.readlines()]
seen  = set()

target = (len(data)-1, len(data[-1])-1)
mappings = {0: (-1, 0), 90: (0, 1), 180: (1, 0), 270: (0, -1)}
queue = [(0, 0, 0, 180, 0)] # heat, i, j, dir, moved_in_dir

while queue:
	heat, i, j, dir, moved_in_dir = heappop(queue)
	if (i, j) == target and moved_in_dir >= 4: break
	if (i, j, dir, moved_in_dir) in seen: continue
	for d in mappings:
		if d == (dir + 180) % 360: continue
		ni, nj = i + mappings[d][0], j + mappings[d][1]
		if ni < 0 or ni > target[0] or nj < 0 or nj > target[1]: continue
		if d == dir:
			if moved_in_dir >= 10: continue
			heappush(queue,(heat + int(data[ni][nj]), ni, nj, d, moved_in_dir+1))
		else:
			if moved_in_dir >= 4 or (i, j) == (0, 0): heappush(queue,(heat + int(data[ni][nj]), ni, nj, d, 1))
	seen.add((i, j, dir, moved_in_dir))
print(heat)
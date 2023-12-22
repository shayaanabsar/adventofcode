from collections import deque
with open('in.txt') as f: data = [line.strip() for line in f.readlines()]

for i, l in enumerate(data):
	for j, c in enumerate(l):
		if c == 'S': start = (i, j)

queue, seen, count = deque([(start, 0)]), set(), 0

while queue:
	curr, steps = queue.popleft()
	if (curr, steps) in seen: continue
	seen.add((curr, steps))
	if steps == 64: 
		count += 1
		continue

	i, j = curr

	for y, x in [(i, j+1), (i, j-1), (i+1, j), (i-1, j)]:
		if 0 <= y < len(data) and 0 <= x < len(data[0]):
			if data[y][x] != '#': queue.append(((y, x), steps + 1))

print(count)

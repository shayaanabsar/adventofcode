from re import findall
from functools import lru_cache

with open('in.txt') as f: data = [line.strip() for line in f.readlines()]

lines = []

for l in data:
	nums = [int(i) for i in findall(r'\d+', l)]
	start, end = nums[:3], nums[3:]
	points = {tuple(end)}

	for d in range(3):
		for s in range(start[d], end[d]):
			point = list(start)
			point[d] = s
			points.add(tuple(point))
	lines.append(points)


lines = sorted(lines, key=lambda line: (min(line, key=lambda point: point[-1])[-1]))
supported = {i: set() for i in range(len(lines))} # a is supported by b
supports  = {i: set() for i in range(len(lines))} # a supports b

def keep_dropping(new_line, i):
	for _, _, z in new_line:
		if z < 1: return False
	found = False
	for j, line in enumerate(lines[:i]):
		if len(line.intersection(new_line)) > 0: 
			supported[i].add(j)
			supports[j].add(i)
			found = True

	return not found

for i, line in enumerate(lines):
	while True:
		new_line = {(x, y, z-1) for x, y, z in line}
		if not keep_dropping(new_line, i): break
		line = new_line
	lines[i] = line

def disintigrate(b, disintigrated):
	queue = []
	for a in supports[b]: 
		if len(supported[a].difference(disintigrated)) == 0:
			queue.append(a)
			disintigrated.add(a)

	for c in queue: disintigrate(c, disintigrated)

	return len(disintigrated) - 1

count = 0
for i in range(len(lines)): count += disintigrate(i, {i})
print(count)

from collections import deque

with open('in.txt') as f: data = [line.strip() for line in f.readlines()]

for i, l in enumerate(data):
	for j, c in enumerate(l):
		if c == 'S': start = (i, j)

def can_visit(allowed_steps):
	queue, seen, count = deque([(start, 0)]), set(), 0

	while queue:
		curr, steps = queue.popleft()
		if (curr, steps) in seen: continue
		seen.add((curr, steps))
		if steps == allowed_steps: 
			count += 1
			continue

		i, j = curr

		for y, x in [(i, j+1), (i, j-1), (i+1, j), (i-1, j)]:
			if data[y % len(data)][x % len(data[0])] != '#': queue.append(((y, x), steps + 1))

	return count

cycle_length = len(data) // 2
size = len(data)

f = [can_visit(cycle_length), can_visit(size + cycle_length), can_visit(size * 2 + cycle_length)]

# polynomial of the form an^2 + bn + c
# f[0] = c
# f[1] = a+b+f[0]
# a = f[1]-f[0]-b

# f[2] = 4a+2b+f[0]
# f[2] = 4f[1]-4f[0]-4b+2b+f[0]
# f[2] = 4f[1]-3f[0]-f[2]-2b
# b    = (4f[1]-3f[0]-f[2])/2

c = f[0]
b = (4*f[1] - 3*f[0] -f[2]) / 2
a = f[1] - f[0] - b

n = (26501365 - cycle_length) / size
print(int(a*(n)**2 + b*n + c))

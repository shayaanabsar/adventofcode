from collections import deque, defaultdict

with open('in.txt') as f: data = [line.strip() for line in f.readlines()]
graph, weighted_graph = defaultdict(lambda : set()), defaultdict(lambda : {})

for i, r in enumerate(data):
	for j, c in enumerate(r):
		if c == '#': continue

		node = (i, j)
		for dy, dx in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
			ni, nj = i+dy, j+dx
			if ni < 0 or ni > len(data) - 1 or nj < 0 or nj > len(data[0]) - 1 or data[ni][nj] == '#': continue
			graph[node].add((ni, nj))

		if i == 0: start = (0, j)
		if i == len(data) - 1: end = (len(data)-1, j)

for node in graph:
	degree = len(graph[node])

	if degree == 0: continue
	if degree > 2 or node == start: 
		queue, seen, original = deque([(node, 0)]), set(), node

		while queue:
			curr, steps = queue.popleft()

			if (len(graph[curr]) > 2 or curr == end) and curr != original: 
				weighted_graph[original][curr] = steps
				continue

			if curr in seen: continue
			seen.add(curr)
			for n in graph[curr]: queue.append((n, steps+1))
			

stack, highest = deque([(start, 0, {start})]), float('-inf')

while stack:
	curr = stack.popleft()
	pos, distance, curr_seen = curr

	if (pos) == end:
		highest = max(highest, distance)
		continue
	
	for n in weighted_graph[pos]: 
		if n not in curr_seen: stack.appendleft((n, distance+weighted_graph[pos][n], curr_seen.union({n})))

print(highest)
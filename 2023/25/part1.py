from collections import defaultdict, deque
from random import choice

with open('in.txt') as f: data = [line.strip() for line in f.readlines()]

graph, edges = defaultdict(lambda: set()), defaultdict(lambda: 0)

for line in data:
	line = line.replace(':', '').split()
	src, targets = line[0], line[1:]

	for t in targets:
		graph[t].add(src)
		graph[src].add(t)

random_pairs = [(choice(list(graph)), choice(list(graph))) for _ in range(1000)]

def bfs(src, target):
	queue, seen = deque([(src, (src,))]), set()

	while queue:
		curr_node, seen_edges = queue.popleft()
		if curr_node in seen: continue
		if curr_node == target: 
			for i in range(len(seen_edges) - 1):
				edges[(seen_edges[i], seen_edges[i+1])] += 1
				edges[(seen_edges[i+1], seen_edges[i])] += 1
			return
		seen.add(curr_node)
		for n in graph[curr_node]: queue.append((n, seen_edges+(n,)))


def find_cycle(original):
	stack, seen = deque([(original)]), set()

	while stack:
		curr = stack.popleft()
		if curr in seen: continue
		seen.add(curr)
		for n in graph[curr]: stack.appendleft(n)
	return len(seen)

for src, target in random_pairs:
	bfs(src, target)

to_remove = sorted(list(edges), key=lambda x:edges[x], reverse=True)[:6]

for src, target in to_remove: graph[src].remove(target)
cycle_1 = find_cycle('ncx')
cycle_2 = len(graph) - cycle_1

print(cycle_1 * cycle_2)
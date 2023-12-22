from collections import deque
from math import lcm
with open('in.txt') as f: data = [line.strip() for line in f.readlines()]

nodes = {'button' : ['broadcaster']}
flip_flops, conjuctions, states = set(), {}, {'button' : False}
connected = None

for l in data:
	l = l.replace(',', '').split()
	match l[0][0]:
		case '%':
			l[0] = l[0][1:]
			flip_flops.add(l[0])
		case '&':
			l[0] = l[0][1:]
			conjuctions[l[0]] = {}
	nodes[l[0]] = l[2:]
	if 'rx' in l[2:]: connected = l[0]

important_nodes = []

for s in dict(nodes):
	for t in nodes[s]:
		if t in conjuctions: conjuctions[t][s] = False
		if connected == t: important_nodes.append(s)
		if t not in states: states[t] = False
		if t not in nodes: nodes[t] = {}

pushes = 0
cycles = [None] * len(important_nodes)

def push_button():
	global pushes
	pushes += 1
	queue, high, low = deque([('button', False)]), 0, 0

	while queue:
		curr, pulse = queue.popleft()

		for t in nodes[curr]:
			if t == connected and pulse and cycles[important_nodes.index(curr)] is None: cycles[important_nodes.index(curr)] = pushes
			if pulse: high += 1
			else: low += 1
			if t in flip_flops:
				if not pulse:
					states[t] = not states[t]
				else: continue
			elif t in conjuctions:
				conjuctions[t][curr] = pulse
				states[t] = not ({True} == set(conjuctions[t].values()))
			else:
				states[t] = pulse
				
			queue.append((t, states[t]))
	return (high, low)


while None in cycles: push_button()
print(lcm(*cycles))
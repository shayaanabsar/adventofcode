from re import findall
from math import lcm

with open('in.txt') as f: data = [line.strip() for line in f.readlines()]

pattern = data[0]
network, current_nodes = {}, []

for line in data[2:]:
	nodes = findall(r'[A-Z0-9]+', line)
	source, targets = nodes[0], nodes[1:]
	network[source] = targets

	if source[-1] == 'A': current_nodes.append(source)

count, mults = 0, [None for _ in current_nodes]

while True:
	if pattern[count % len(pattern)] == 'L': idx = 0
	else: idx = 1

	for i, node in enumerate(current_nodes):
		current_nodes[i] = network[node][idx]
		if current_nodes[i][-1] == 'Z' and mults[i] == None:
			mults[i] = count + 1

	if None not in mults: break
	count += 1

print(lcm(*mults))
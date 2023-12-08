from re import findall

with open('in.txt') as f: data = [line.strip() for line in f.readlines()]

pattern = data[0]
network = {}

for line in data[2:]:
	nodes = findall(r'[A-Z]+', line)
	source, targets = nodes[0], nodes[1:]
	network[source] = targets

current_node, count = 'AAA', 0

while current_node != 'ZZZ':
	if pattern[count % len(pattern)] == 'L': idx = 0
	else: idx = 1

	current_node = network[current_node][idx]

	count += 1
print(count)
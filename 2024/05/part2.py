from collections import defaultdict
from copy import copy

with open('in.txt') as f: data = [line.strip() for line in f.readlines()]

before = defaultdict(lambda : set())
updates = []

def sort(update):
	update = copy(update)
	
	for i in range(len(update)):
		for j in range(i+1, len(update)):
			n, m = update[i], update[j]
			if m in before[n]:
				update[j], update[i] = update[i], update[j]
	return update

for line in data:
	if '|' in line:
		x, y = [int(i) for i in line.split('|')]
		before[y].add(x)
	elif line != '':
		updates.append([int(i) for i in line.split(',')])

ans = 0
for update in updates:
	sorted_update = sort(update)
	if update != sorted_update:
		ans += sorted_update[len(sorted_update) // 2]

print(ans)
from collections import defaultdict

with open('in.txt') as f: data = [line.strip() for line in f.readlines()]

before = defaultdict(lambda : set())
updates = []

for line in data:
	if '|' in line:
		x, y = [int(i) for i in line.split('|')]
		before[y].add(x)
	elif line != '':
		updates.append([int(i) for i in line.split(',')])
ans = 0
for update in updates:
	works = True
	for i, n in enumerate(update):
		if before[n].intersection(set(update[i:])) != set():
			works = False; break
	if works: ans += update[len(update) // 2]
print(ans)
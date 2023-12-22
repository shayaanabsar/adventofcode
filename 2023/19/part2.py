from re import findall
from copy import deepcopy
from collections import deque
from math import prod

with open('in.txt') as f: data = [line.strip() for line in f.readlines()]

workflows = {}

def parse_workflow(line):
	name, conditions = line[0], line[1:]
	workflow = []
	for i in range(0, len(conditions), 3):
		try:
			sign, num = conditions[i+1][0], int(conditions[i+1][1:])
			workflow.append((conditions[i], sign, num, conditions[i+2]))
		except IndexError: workflow.append((conditions[i],))
	workflows[name] = workflow
	
for line in data:
	if line == '': break
	line = findall(r'[<>]*\w+', line)
	parse_workflow(line)

pindex = lambda x: 'xmas'.index(x)
queue = deque([[(1, 4000), (1, 4000), (1, 4000), (1, 4000), 'in']])
works = set()
seen = set()
total = 0

while queue:
	curr = queue.popleft()
	if curr[-1] == 'A':
		unique_combinations = prod([(e - s + 1) for s, e in curr[:-1]])
		for s in works:
			overlaps = []
			not_overlapping = []

			for i in range(4):
				s1, e1 = curr[i]
				s2, e2 = s[i]
				o_s, o_e = max(s1, s2), min(e1, e2)
				o_size = max(0, o_e - o_s + 1)
				overlaps.append(o_size)
			
			unique_combinations -= prod(overlaps)
		total += unique_combinations
		works.add(tuple(curr))
		continue

	elif curr[-1] == 'R': continue
	if tuple(curr) in seen: continue
	seen.add(tuple(curr))
	done = False
	
	
	for rule in workflows[curr[-1]]:
		if len(rule) == 1:
			new = deepcopy(curr)
			new[-1] = rule[0]
			queue.append(new)
			break
			
		p, sign, num, new_workflow = rule

		s, e     = curr[pindex(p)]
		if sign == '>': r_s, r_e = num+1, 4000
		elif sign == '<': r_s, r_e = 1, num - 1

		overlap_start, overlap_end = max(s, r_s), min(e, r_e)
		
		if overlap_start < overlap_end:
			new = deepcopy(curr)
			new[pindex(p)] = (overlap_start, overlap_end)
			new[-1] = new_workflow
			done = True
			queue.append(new)
		if overlap_start > s:
			new = deepcopy(curr)
			new[pindex(p)] = (s, overlap_start - 1)
			queue.append(new)
		elif overlap_end < e:
			new = deepcopy(curr)
			new[pindex(p)] = (overlap_end + 1, e)
			queue.append(new)

		if done: break

print(total)
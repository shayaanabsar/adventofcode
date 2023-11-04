from collections import deque
from copy import deepcopy, copy
from itertools import permutations

map = {}
flow_rates = {}

with open('in.txt', 'r') as f:
	data = f.readlines()
	for line in data:
		line = line.strip('\n').replace(';', ' ').replace(',', '').split()
		valve, flow_rate, leading_to = line[1], int(line[4][5:]), line[9:]
		map[valve] = set(leading_to)
		flow_rates[valve] = flow_rate

valves = list(flow_rates.keys())

distances = {}

for i in range(len(valves)):
	for j in range(len(valves)):
		if i == j:
			distances[(valves[i], valves[j])] = 0
		elif valves[j] in map[valves[i]]:
			distances[(valves[i], valves[j])] = 1
		else:
			distances[(valves[i], valves[j])] = float('inf')

for k in range(len(valves)):
	for i in range(len(valves)):
		for j in range(len(valves)):
			distances[(valves[i], valves[j])] = min(distances[(valves[i], valves[j])],
													distances[(valves[i], valves[k])] + distances[(valves[k], valves[j])]
			)

class State:
	def __init__(self, curr_valve, open_valves, time, flow):
		self.curr_valves = curr_valve
		self.open_valves = open_valves
		self.times = time
		self.flow = flow
	
	def __repr__(self):
		return f'(curr_valve: {self.curr_valves}, open_valves: {self.open_valves}, time: {self.times}, flow: {self.flow})'

queue = deque()
queue.append(State(['AA', 'AA'], set(), [0, 0], 0))
highest = float('-inf')
valves = set(filter(lambda v: flow_rates[v] > 0, valves))
seen_moves = set()

while queue:
	curr = queue.popleft()

	if curr.times[0] >= 26 and curr.times[1] >= 26:
		continue

	possible_valves = list(set(valves).difference(curr.open_valves.union(curr.curr_valves)))

	if curr.times[0] >= 26:
		combos = [['FINISHED', i] for i in possible_valves]
	elif curr.times[1] >= 26:
		combos = [[i, 'FINISHED'] for i in possible_valves]
	else:
		combos = list(permutations(possible_valves, 2))

	for c in combos:
		old_a, old_b, new_a, new_b = (*curr.curr_valves, *c)
		new_times, new_flow = copy(curr.times), curr.flow

		move = ((new_flow), (new_a, new_b))

		if move in seen_moves: 
			continue
		seen_moves.add(move)

		if new_a != 'FINISHED': 
			new_times[0] += distances[(curr.curr_valves[0], new_a)] + 1
			new_flow += ((26 - new_times[0]) * flow_rates[new_a])
		if new_b != 'FINISHED': 
			new_times[1] += distances[(curr.curr_valves[1], new_b)] + 1
			new_flow += ((26 - new_times[1]) * flow_rates[new_b])

		queue.append(State(
			[new_a, new_b],
			curr.open_valves.union({new_a, new_b}),
			new_times,
			new_flow
		))
		
	highest = max(highest, curr.flow)
print(highest)
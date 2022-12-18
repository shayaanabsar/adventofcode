from collections import deque
from copy import deepcopy

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
		self.curr_valve = curr_valve
		self.open_valves = open_valves
		self.time = time
		self.flow = flow
	
	def __repr__(self):
		return f'(curr_valve: {self.curr_valve}, open_valves: {self.open_valves}, time: {self.time}, flow: {self.flow})'

queue = deque()
queue.append(State('AA', set(), 0, 0))

for valve in deepcopy(valves):
	if flow_rates[valve] == 0:
		valves.remove(valve)


highest = float('-inf')

while queue:
	curr = queue.popleft()

	if curr.time >= 30:
		continue

	for valve in valves:
		if valve != curr.curr_valve and valve not in curr.open_valves:
			new_time = curr.time + distances[(curr.curr_valve, valve)] + 1

			queue.append(State(
				valve,
				curr.open_valves.union({valve}),
				new_time,
				curr.flow + ((30 - new_time) * flow_rates[valve])
			))

	highest = max(highest, curr.flow)
print(highest)
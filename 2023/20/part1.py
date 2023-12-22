from collections import deque
with open('in.txt') as f: data = [line.strip() for line in f.readlines()]

nodes = {'button' : ['broadcaster']}
flip_flops, conjuctions, states = set(), {}, {'button' : False}


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

for s in dict(nodes):
	for t in nodes[s]:
		if t in conjuctions: conjuctions[t][s] = False
		if t not in states: states[t] = False
		if t not in nodes: nodes[t] = {}


def push_button():
	queue, high, low = deque([('button', False)]), 0, 0

	while queue:
		curr, pulse = queue.popleft()

		for t in nodes[curr]:
			#print(f'{curr} -{pulse}-> {t}')
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

high, low = 0, 0

for i in range(1000):
	curr = push_button()
	high += curr[0]
	low  += curr[1] 

print(high * low)
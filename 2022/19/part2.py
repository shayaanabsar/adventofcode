from collections import deque
from copy import deepcopy
from functools import lru_cache



costs = [
		[0,0,0,0],
		[0,0,0,0],
		[0,0,0,0],
		[0,0,0,0]
]

types = ['ore', 'clay', 'obsidian', 'geode']
max_number = [0,0,0,float('inf')]

def git_rid_of_extra(state):
	ore_r, clay_r, obsidian_r, geode_r, ore_c, clay_c, obsidian_c, geode_c, time = state

	ore_c += ore_r
	clay_c += clay_r
	obsidian_c += obsidian_r
	geode_c += geode_r

	time_left = 32 - time

	if ore_c > (time_left * max_number[0]):
		ore_c = time_left * max_number[0]
	if clay_c > (time_left * max_number[1]):
		clay_c = time_left * max_number[1]
	if obsidian_c > (time_left * max_number[2]):
		obsidian_c = time_left * max_number[2]
	return (ore_r, clay_r, obsidian_r, geode_r, ore_c, clay_c, obsidian_c, geode_c, time)

def options(state):
	ore_r, clay_r, obsidian_r, geode_r, ore_c, clay_c, obsidian_c, geode_c, time = state
	options = []

	if ore_r < max_number[0]:
		new_state = [ore_r, clay_r, obsidian_r, geode_r, ore_c, clay_c, obsidian_c, geode_c, time+1]
		can_buy = True
		for i in range(4):
			new_state[i+4] -= costs[0][i]
			if new_state[i+4] < 0:
				can_buy = False
		new_state[0] += 1
		new_state[4] -= 1
		if can_buy:
			options.append(git_rid_of_extra(tuple(new_state)))
	if clay_r < max_number[1]:
		new_state = [ore_r, clay_r, obsidian_r, geode_r, ore_c, clay_c, obsidian_c, geode_c, time+1]
		can_buy = True
		for i in range(4):
			new_state[i+4] -= costs[1][i]
			if new_state[i+4] < 0:
				can_buy = False
		new_state[1] += 1
		new_state[5] -= 1
		if can_buy:
			options.append(git_rid_of_extra(tuple(new_state)))
	if obsidian_r < max_number[2]:
		new_state = [ore_r, clay_r, obsidian_r, geode_r, ore_c, clay_c, obsidian_c, geode_c, time+1]
		can_buy = True
		for i in range(4):
			new_state[i+4] -= costs[2][i]
			if new_state[i+4] < 0:
				can_buy = False
		new_state[2] += 1
		new_state[6] -= 1
		if can_buy:
			options.append(git_rid_of_extra(tuple(new_state)))
	if geode_r < max_number[3]:
		new_state = [ore_r, clay_r, obsidian_r, geode_r, ore_c, clay_c, obsidian_c, geode_c, time+1]
		can_buy = True
		for i in range(4):
			new_state[i+4] -= costs[3][i]
			if new_state[i+4] < 0:
				can_buy = False
		new_state[3] += 1
		new_state[7] -= 1
		if can_buy:
			options.append(git_rid_of_extra(tuple(new_state)))

	options.append(git_rid_of_extra((ore_r, clay_r, obsidian_r, geode_r, ore_c, clay_c, obsidian_c, geode_c, time+1)))

	return options

def dfs():
	original_state = (1, 0, 0, 0, 0, 0, 0, 0, 0)
	stack = deque([original_state])
	dp = {}
	highest = 0

	while stack:
		curr = stack.popleft()
		if curr[-1] > 32:
			continue
		if curr in dp:
			continue
		dp[curr] = curr[-2]
		highest = max(highest, curr[-2])
		for option in options(curr):
			stack.appendleft(option)
	return highest


with open('in.txt') as f:
	data = f.readlines()
	prod = 1

	for bpr_num, line in enumerate(data):
		line = line.strip('\n').split(':')[1].split('.')
		
		for sentence in line:
			sentence = sentence.strip().split()
			try:
				robot_type = types.index(sentence[1])
			except IndexError:
				break
			
			for i in range(4):
				rock = types[i]
				if rock in sentence[2:]:
					costs[robot_type][i] = int(sentence[sentence[2:].index(rock)+1])
					max_number[i] = max(max_number[i], costs[robot_type][i])
		geodes = dfs()

		prod *= geodes
print(prod)

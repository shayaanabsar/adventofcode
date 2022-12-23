from collections import deque
from copy import deepcopy

elf_positions = set()

with open('in.txt') as f:
	data = f.readlines()

	for i, line in enumerate(data):
		line = line.strip('\n')
		for j, char in enumerate(line):
			if char == '#':
				elf_positions.add((i, j))


def check_adjacent(elf_pos):
	i, j = elf_pos
	adjacent = set()

	for x in range(-1, 2):
		adjacent.add((i-1, j+x))
		adjacent.add((i, j+x))
		adjacent.add((i+1, j+x))

	return adjacent.intersection(elf_positions) == {elf_pos}

def check_proposition(elf_pos, direction):
	i, j = elf_pos

	match direction:
		case 0: # North
			elfs = {(i-1, j), (i-1, j+1), (i-1, j-1)}
		case 1: # South
			elfs = {(i+1, j), (i+1, j+1), (i+1, j-1)}
		case 2: # West
			elfs = {(i, j-1), (i-1, j-1), (i+1, j-1)}
		case 3: # East
			elfs = {(i, j+1), (i-1, j+1), (i+1, j+1)}

	return len(elfs.intersection(elf_positions)) == 0

directions = deque([0, 1, 2, 3])
previous_elves = None
round  = 0

while previous_elves != elf_positions:
	previous_elves = deepcopy(elf_positions)

	propositions = {}

	for elf in elf_positions:
		if check_adjacent(elf):
			continue

		done = False
		for i in directions:
			if check_proposition(elf, i):
				done = True
				break
		if not done:
			continue

		y, x = elf
		
		match i:
			case 0:
				new_pos = (y-1, x)
			case 1:
				new_pos = (y+1, x)
			case 2:
				new_pos = (y, x-1)
			case 3:
				new_pos = (y, x+1)
		
		propositions[elf] = new_pos

	new_positions = list(propositions.values())
	
	for previous in propositions:
		new_pos = propositions[previous]
		if new_positions.count(new_pos) == 1:
			elf_positions.remove(previous)
			elf_positions.add(new_pos)
		
	directions.append(directions.popleft())
	round += 1

print(round)

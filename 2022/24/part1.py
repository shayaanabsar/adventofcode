from collections import deque

with open('in.txt') as f:
	data = [line.strip('\n')[1:-1] for line in f.readlines()][1:-1]
	blizzards = []

	for i, line in enumerate(data):
		for j, char in enumerate(line):
			if char in '^><v':
				blizzards.append((i, j, char))
	

start = (-1, 0)
end = (len(data), len(data[0]) - 1)

def get_blizzard_set(curr_blizzards):
	return {(i, j) for i, j, _ in curr_blizzards}


def move_blizzards(curr_blizzards):
	new_blizzards = []

	for blizzard in curr_blizzards:
		i, j, dir = blizzard
		
		match dir:
			case '>':
				j += 1
			case '<':
				j -= 1
			case '^':
				i -= 1
			case 'v':
				i += 1
	
		i %= len(data)
		j %= len(data[0])

		new_blizzards.append((i, j, dir))
	return new_blizzards

def get_neighbours(curr, time, blizzards):
	blizzard_set = get_blizzard_set(move_blizzards(blizzards))
	
	i, j = curr

	poss_neighbours = [
		(i+1, j),
		(i-1, j),
		(i, j-1),
		(i, j+1),
		(i, j)
	]
	act_neighbours = []

	for neighbour in poss_neighbours:
		i, j = neighbour
		if (neighbour not in blizzard_set and ((0 <= i < len(data)) and (0 <= j < len(data[0])))) or (neighbour == end) or (curr == start and neighbour == start):
			act_neighbours.append((neighbour, time+1))

	return act_neighbours

queue = deque()
queue.append((start, 0))
blizzard_positions = {0: blizzards}
seen = set()

while queue:
	curr, time = queue.popleft()

	if time not in blizzard_positions:
		blizzard_positions[time] = move_blizzards(blizzard_positions[time-1])
	if (curr, tuple(get_blizzard_set(blizzard_positions[time]))) in seen:
		continue
	seen.add((curr, tuple(get_blizzard_set(blizzard_positions[time]))))
	
	if curr == end:
		print(time)
		break
	
	for neighbour in get_neighbours(curr, time, blizzard_positions[time]):
		queue.append(neighbour)

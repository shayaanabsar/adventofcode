from collections import defaultdict

with open('in.txt') as f:
	pattern = f.readline()



rocks = [
	'####',
	' # \n###\n # ',
	'  #\n  #\n###',
	'#\n#\n#\n#',
	'##\n##'
]

rocks = [r.split('\n')[::-1] for r in rocks]

def move(positions, i_change, j_change):
	done, new_positions = True,[]

	for (i, j) in positions:
		new_positions.append((i+i_change, j+j_change))

		if grid[(i+i_change, j+j_change)] == '#' or i+i_change < 0 or j+j_change > 6 or j+j_change < 0:
			if j_change != 0:
				return (True, positions)
			return (False, positions)

	return (True, new_positions)

def shift_left(positions): return move(positions, 0, -1)
def shift_right(positions): return move(positions, 0, 1)
def shift_down(positions): return move(positions, -1, 0) 


grid = defaultdict(lambda : '.')
highest, pattern_count = -1, 0
increments = []

for rock_count in range(2023):
	rock = rocks[rock_count % 5]
	j_offset, k_offset = highest+4, 2
	positions = []

	for j, row in enumerate(rock):
		for k, char in enumerate(row):
			if char == '#': positions.append((j+j_offset, k+k_offset))
	keep_dropping=True
	while keep_dropping:
		direction = pattern[pattern_count%len(pattern)]
		if direction == '>': _, positions = shift_right(positions)
		else: _, positions = shift_left(positions)
		keep_dropping, positions = shift_down(positions)
		pattern_count += 1
	old_highest = highest
	highest = max(highest, max(positions, key=lambda x: x[0])[0])
	increments.append(highest-old_highest)

	for position in positions: grid[position] = '#'
	rock_count += 1

patterns = {}
for i, v in enumerate(increments):
	sub = tuple(increments[i:i+100])
	if sub in patterns:
		break
	patterns[sub] = i

pattern = increments[patterns[sub]:i]
total = sum(increments[:patterns[sub]])

full_patterns = (1000000000000 - patterns[sub]) // len(pattern)
extra = (1000000000000 - patterns[sub]) % len(pattern)

total += (full_patterns * sum(pattern))
total += sum(pattern[:extra])

print(total)

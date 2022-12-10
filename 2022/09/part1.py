with open('in.txt', 'r') as file:
	data = file.readlines()

head_pos = [4, 0]
tail_pos = [4, 0]

def is_touching():
	global head_pos
	global tail_pos

	if tail_pos[0] == head_pos[0]:
		if tail_pos[1] + 1 == head_pos[1]:
			return True
		if tail_pos[1] - 1 == head_pos[1]:
			return True
	if tail_pos[1] == head_pos[1]:
		if tail_pos[0] + 1 == head_pos[0]:
			return True
		elif tail_pos[0] - 1 == head_pos[0]:
			return True
	
	test_diagonals = [(+1, +1), (+1, -1), (-1, +1), (-1, -1)]

	for i, j in test_diagonals:
		if tail_pos[0] + i == head_pos[0] and tail_pos[1] + j == head_pos[1]:
			return True
	
	if tail_pos == head_pos:
		return True
	return False

def make_diagonal():
	global head_pos
	global tail_pos

	test_diagonals = [(+1, +1), (+1, -1), (-1, +1), (-1, -1)]

	for i, j  in test_diagonals:
		tail_pos[0] += i
		tail_pos[1] += j

		if is_touching():
			return
		
		tail_pos[0] -= i
		tail_pos[1] -= j


def make_move():
	global head_pos
	global tail_pos

	if tail_pos[0] == head_pos[0]:
		if tail_pos[1] + 2 == head_pos[1]:
			tail_pos[1] += 1
			return
		elif tail_pos[1] - 2 == head_pos[1]:
			tail_pos[1] -= 1
			return
	if tail_pos[1] == head_pos[1]:
		if tail_pos[0] + 2 == head_pos[0]:
			tail_pos[0] += 1
			return
		elif tail_pos[0] - 2 == head_pos[0]:
			tail_pos[0] -= 1
			return
	make_diagonal()

positions = set()

for line in data:
	line = line.strip('\n').split(' ')
	direction, amount = line
	amount = int(amount)

	for i in range(amount):
		if direction == 'L':
			head_pos[1] -= 1
		elif direction == 'R':
			head_pos[1] += 1
		elif direction == 'U':
			head_pos[0] -= 1
		elif direction == 'D':
			head_pos[0] += 1
		
		if not is_touching():
			make_move()

		positions.add(tuple(tail_pos))

print(len(positions))
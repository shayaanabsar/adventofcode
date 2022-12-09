with open('in.txt', 'r') as file:
	data = file.readlines()

knots = []

for i in range(10):
	knots.append([4, 0])
	
def is_touching(a, b):
	if knots[b][0] == knots[a][0]:
		if knots[b][1] + 1 == knots[a][1]:
			return True
		if knots[b][1] - 1 == knots[a][1]:
			return True
	if knots[b][1] == knots[a][1]:
		if knots[b][0] + 1 == knots[a][0]:
			return True
		elif knots[b][0] - 1 == knots[a][0]:
			return True
	
	test_diagonals = [(+1, +1), (+1, -1), (-1, +1), (-1, -1)]

	for i, j in test_diagonals:
		if knots[b][0] + i == knots[a][0] and knots[b][1] + j == knots[a][1]:
			return True
	
	if knots[b] == knots[a]:
		return True
	return False

def make_diagonal(a, b):
	test_diagonals = [(+1, +1), (+1, -1), (-1, +1), (-1, -1)]

	for i, j  in test_diagonals:
		knots[b][0] += i
		knots[b][1] += j

		if is_touching(a, b):
			return
		
		knots[b][0] -= i
		knots[b][1] -= j


def make_move(a, b):
	if knots[b][0] == knots[a][0]:
		if knots[b][1] + 2 == knots[a][1]:
			knots[b][1] += 1
			return
		elif knots[b][1] - 2 == knots[a][1]:
			knots[b][1] -= 1
			return
	if knots[b][1] == knots[a][1]:
		if knots[b][0] + 2 == knots[a][0]:
			knots[b][0] += 1
			return
		elif knots[b][0] - 2 == knots[a][0]:
			knots[b][0] -= 1
			return
	make_diagonal(a, b)

positions = set()

for line in data:
	line = line.strip('\n').split(' ')
	direction, amount = line
	amount = int(amount)

	for i in range(amount):
		if direction == 'L':
			knots[0][1] -= 1
		elif direction == 'R':
			knots[0][1] += 1
		elif direction == 'U':
			knots[0][0] -= 1
		elif direction == 'D':
			knots[0][0] += 1
		
		for j in range(1, 10):
			if not is_touching(j-1, j):
				make_move(j-1, j)

		positions.add(tuple(knots[-1]))

print(len(positions))
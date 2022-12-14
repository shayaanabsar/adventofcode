from collections import defaultdict

with open('in.txt', 'r') as file:
	data = file.readlines()

grid = defaultdict(lambda: '.')

def draw_line(a, b):
	if a[1] == b[1]:
		start = min(a[0], b[0])
		end = max(a[0], b[0])

		for i in range(start, end+1):
			grid[(i, a[1])] = '#'
	elif a[0] == b[0]:
		start = min(a[1], b[1])
		end = max(a[1], b[1])

		for i in range(start, end+1):
			grid[(a[0], i)] = '#'

MAX_X = float('-inf')
MAX_Y = float('-inf')

for line in data:
	line = line.strip('\n').split('->')
	
	for i in range(len(line)):
		x, y = line[i].split(',')
		line[i] = (int(x), int(y))

		MAX_X = max(MAX_X, int(x))
		MAX_Y = max(MAX_Y, int(y))
	
	for i in range(len(line) - 1):
		draw_line(line[i], line[i+1])

def move_sand_particle():
	x, y = 500, 0
	made_move = True

	while made_move:
		made_move = False

		if grid[(x, y+1)] == '.':
			y += 1
			made_move = True
		elif grid[(x-1, y+1)] == '.':
			x -= 1
			y += 1
			made_move = True
		elif grid[(x+1, y+1)] == '.':
			x += 1
			y += 1
			made_move = True
	
		if x > MAX_X or y > MAX_Y or y < 0 or x < 0:
			return False

	grid[(x, y)] = 'o'

count = 0

while True:
	if move_sand_particle() != False:
		count += 1
	else:
		break

print(count)
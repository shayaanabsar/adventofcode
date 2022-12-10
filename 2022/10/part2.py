with open('in.txt', 'r') as file:
	data = file.readlines()

cycle_count = 0
x = 1
crt = [' ' for i in range(240)]
sprite_pos = [0, 1, 2]

def draw():
	global cycle_count

	if (cycle_count % 40) - 1 in sprite_pos:
		crt[cycle_count - 1] = '#'


for line in data:
	line = line.strip('\n').split()

	if line[0] == 'addx':
		cycle_count += 1
		draw()
		cycle_count += 1
		draw()
		x += int(line[1])
	else:
		cycle_count += 1
		draw()
	
	sprite_pos = [x-1, x, x+1]

for i, c in enumerate(crt):
	print(c, end='')

	if i % 40 == 39:
		print('')

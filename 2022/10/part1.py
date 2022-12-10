with open('in.txt', 'r') as file:
	data = file.readlines()

cycle_count = 1
x = 1
strength = 0

for line in data:
	line = line.strip('\n').split()
	cycle_count_before = cycle_count

	if line[0] == 'addx':
		x += int(line[1])
		cycle_count += 2
	else:
		cycle_count += 1

	a = 0
	
	if cycle_count == 20 or (cycle_count_before + 1) == 20:
		strength += x * cycle_count
	elif (cycle_count - 20) % 40 == 0:
		strength += x * cycle_count
	elif (cycle_count_before - 20) % 40 == 39:
		strength += (x - int(line[1])) * (cycle_count_before + 1)

print(strength)

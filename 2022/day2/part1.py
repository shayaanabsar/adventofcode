with open('in.txt', 'r') as file:
	data = file.readlines()

points = 0
for row in data:
	row=row.strip('\n')
	opp, me = [_ for _ in row.split()]

	if me == 'X':
		points += 1
		if opp == 'C':
			points += 6
		if opp == 'A':
			points += 3
	elif me == 'Y':
		points += 2
		if opp == 'A':
			points += 6
		if opp == 'B':
			points += 3
	else:
		points += 3
		if opp == 'B':
			points += 6
		if opp == 'C':
			points += 3

print(points)

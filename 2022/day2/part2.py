with open('in.txt', 'r') as file:
	data = file.readlines()

points = 0
for row in data:
	row=row.strip('\n')
	opp, end = [_ for _ in row.split()]

	choose = ''
	if opp == 'A':
		if end == 'X':
			choose = 'Scissors'
		elif end == 'Y':
			choose = 'Rock'
		else:
			choose = 'Paper'

	elif opp == 'B':
		if end == 'X':
			choose = 'Rock'
		elif end == 'Y':
			choose = 'Paper'
		else:
			choose = 'Scissors'

	else:
		if end == 'X':
			choose = 'Paper'
		elif end == 'Y':
			choose = 'Scissors'
		else:
			choose = 'Rock'

	points_scheme  = {
		'Rock': 1,
		'Paper': 2,
		'Scissors': 3,

		'X': 0,
		'Y': 3,
		'Z': 6
	}

	points += (points_scheme[choose] + points_scheme[end])

print(points)

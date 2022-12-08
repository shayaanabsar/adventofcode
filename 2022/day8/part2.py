with open('in.txt', 'r') as file:
	data = file.readlines()

	for i in range(len(data)):
		data[i] = data[i].strip('\n')
		data[i] = [int(j) for j in list(data[i])]

highest = float('-inf')

for i, col in enumerate(data):
	for j, val in enumerate(col):
		left = data[i][:j]
		right = data[i][j+1:]

		up = []
		for x in range(i):
			up.append(data[x][j])
		up = up
		down = []
		for x in range(i+1, len(data)):
			down.append(data[x][j])

		dirs = [up[::-1], down, left[::-1], right]
		score = 1
		for dir in dirs:
			count = 1

			if dir == []:
				score = 0
				break
			
			for num in dir:
				if data[i][j] > num:
					count += 1
				else:
					break
			count = min(len(dir), count)
			score *= count
		highest = max(highest, score)

print(highest)
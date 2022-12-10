with open('in.txt', 'r') as file:
	data = file.readlines()

	for i in range(len(data)):
		data[i] = data[i].strip('\n')
		data[i] = [int(j) for j in list(data[i])]

count = 0

for i, col in enumerate(data):
	for j, val in enumerate(col):
		left = data[i][:j+1]
		right = data[i][j:]

		up = []
		for x in range(i+1):
			up.append(data[x][j])
		
		down = []
		for x in range(i, len(data)):
			down.append(data[x][j])

		dirs = [up, down, left, right]

		for dir in dirs:
			if max(dir) == data[i][j] and dir.count(data[i][j]) == 1:
				count += 1
				break

print(count)
		
with open('in.txt') as f: data = [list(line.strip()) for line in f.readlines()]
total = 0

for i, r in enumerate(data):
	for j, c in enumerate(r):
		if c == 'O':
			curr_i = i
			while curr_i - 1 >= 0 and data[curr_i-1][j] == '.' : curr_i -= 1
			data[i][j], data[curr_i][j] = '.', 'O'
			total += (len(data) - curr_i)

print(total)
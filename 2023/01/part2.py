from re import finditer

with open('in.txt', 'r') as file:
	data = file.readlines()

digs = ['zero','one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', r'\d']
sum = 0

for l in data:
	numbers = []

	for d in digs:
		numbers += [(i.group(), i.start()) for i in finditer(d, l.strip())]

	numbers.sort(key=lambda x: x[1])
	a, b = numbers[0][0], numbers[-1][0]

	if a in digs: a = digs.index(a)
	if b in digs: b = digs.index(b)

	sum += int(a) * 10 + int(b)

print(sum)
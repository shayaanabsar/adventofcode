with open('in.txt') as f: data = f.read().split(',')

total = 0
for word in data:
	current_total = 0
	for c in word:
		current_total += ord(c)
		current_total *= 17
		current_total %= 256
	total += current_total
print(total)
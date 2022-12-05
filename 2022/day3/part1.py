import string

with open('in.txt', 'r') as file:
	data = file.readlines()


alphabet = string.ascii_lowercase
priority = 0

for line in data:
	line = line.strip('\n')

	pack1, pack2 = line[:len(line)//2], line[len(line)//2:]
	
	for char in pack1:
		if char in pack2:
			break

	priority += alphabet.index(char.lower()) + 1

	if char.isupper():
		priority += 26
	
print(priority)

with open('in.txt', 'r') as file:
	data = file.readlines()

count = 0

for line in data:
	elf1, elf2 = line.strip('\n').split(',')

	start, end = [int(_) for _ in elf1.split('-')]
	elf1 = {i for i in range(start, end+1)}

	start, end = [int(_) for _ in elf2.split('-')]
	elf2 = {i for i in range(start, end+1)}


	if len(elf1.intersection(elf2)) >= 1:
		count += 1

print(count)
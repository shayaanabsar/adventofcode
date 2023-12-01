from re import findall

with open('in.txt', 'r') as file:
	data = file.readlines()

sum = 0

for l in data:
	numbers = findall(r'\d', l.strip())
	sum += int(numbers[0][-1]) * 10 + int(numbers[-1][-1])

print(sum)
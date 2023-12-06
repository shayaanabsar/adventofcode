from re import findall
from math import ceil, sqrt

with open('in.txt') as f: data = [line.strip() for line in f.readlines()]

times     = [int(i) for i in findall(r'\d+', data[0])]
distances = [int(i) for i in findall(r'\d+', data[1])]
total = 1

for i, time in enumerate(times):
	root1 = ceil((times[i] + sqrt(time ** 2 - 4 * distances[i])) / 2)
	root2 = ceil((times[i] - sqrt(times[i] ** 2 - 4 * distances[i])) / 2)
	total *= abs(root1-root2)
print(total)
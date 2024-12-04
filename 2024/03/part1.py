import re

with open('in.txt') as f: data = [line.strip() for line in f.readlines()]
ans = 0
for l in data:
	for x, y in re.findall(r'mul\((\d+),(\d+)\)', l): 
		ans += (int(x)*int(y))
print(ans)
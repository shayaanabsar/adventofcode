import re

with open('in.txt') as f: data = [line.strip() for line in f.readlines()]
ans, enabled = 0, True
for l in data:
	muls = re.findall(r'mul\(\d+,\d+\)|don\'t|do', l)
	for m in muls:
		if m == 'do': enabled = True
		elif m == 'don\'t': enabled = False
		elif enabled:
			m = m.split(',')
			x, y = int(m[0][4:]), int(m[1][:-1])
			ans += (x*y)

print(ans)
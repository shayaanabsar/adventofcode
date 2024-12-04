with open('in.txt') as f: data = [[int(i) for i in line.strip().split()] for line in f.readlines()]
safe = 0
for r in data:
	if sorted(r) != r and sorted(r, reverse=True) != r: continue
	prev, works = r[0], True

	for n in r[1:]:
		if abs(prev - n) < 1 or abs(prev - n) > 3:
			works = False
			break
		prev = n
	if works: safe += 1

print(safe)
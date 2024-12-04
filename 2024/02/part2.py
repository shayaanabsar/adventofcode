with open('in.txt') as f: data = [[int(i) for i in line.strip().split()] for line in f.readlines()]
safe = 0
for r in data:
	for i, _ in enumerate(r):
		r_prime = r[:i] + r[i+1:]

		if sorted(r_prime) != r_prime and sorted(r_prime, reverse=True) != r_prime: continue
		prev, works = r_prime[0], True

		for n in r_prime[1:]:
			if abs(prev - n) < 1 or abs(prev - n) > 3:
				works = False
				break
			prev = n
		if works: 
			safe += 1
			break

print(safe)
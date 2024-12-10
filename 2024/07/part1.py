with open('in.txt') as f: data = [line.strip() for line in f.readlines()]
works = 0

def create_strings(n):
	if n == 1: return ['0', '1']

	s = create_strings(n-1)
	s_prime = []
	for n in s:
		s_prime.append(n + '0')
		s_prime.append(n + '1')
	
	return s_prime


for line in data:
	target, rest = line.split(':')
	target, rest = int(target), [int(i) for i in rest.split()]
	
	operators = len(rest) - 1

	for s in create_strings(operators):
		if s[0] == '0': total = rest[0] * rest[1]
		if s[0] == '1': total = rest[0] + rest[1]

		s_count = 1

		for j in range(2, len(rest)):
			if s[s_count] == '0': total *= rest[j]
			if s[s_count] == '1': total += rest[j]
			
			s_count += 1
		
		if total == target:
			works += target
			break

print(works)

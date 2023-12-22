from functools import lru_cache

with open('in.txt') as f: data = [line.strip() for line in f.readlines()]

@lru_cache
def count(pattern, nums):
	if pattern == '': return 1 if nums == () else 0
	if nums    == (): return 1 if '#' not in pattern else 0
	quant, start = 0, pattern[0]

	if start in '.?': quant += count(pattern[1:], nums)
	if start in '#?':
		if len(pattern) >= nums[0] and '.' not in pattern[:nums[0]] and pattern[nums[0]] != '#': 
				quant += count(pattern[nums[0] + 1:], nums[1:])
	
	return quant

total = 0

for line in data:
	pattern, nums = line.split()
	nums = tuple(int(i) for i in nums.split(',')) * 5
	pattern = (pattern + '?') * 5
	pattern = pattern[:-1]
	total += count(pattern + '.', nums)

print(total)
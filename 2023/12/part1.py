with open('in.txt') as f: data = [line.strip() for line in f.readlines()]

def is_valid(pattern, replacements, nums):
	hash_length, nums_count, replacement_count, in_seq = 0, 0, 0, False
	
	for i, c in enumerate(pattern):
		if c == '?':
			if replacement_count >= len(replacements):
				return True
			c = replacements[replacement_count]
			replacement_count += 1
		if c == '#':
			hash_length += 1
			in_seq = True
		elif c == '.':
			if in_seq:
				if nums_count >= len(nums): return False
				if hash_length != nums[nums_count]: return False
				hash_length, in_seq = 0, False
				nums_count += 1
	return nums_count >= len(nums)

total = 0

def count(pattern, replacements, nums):
	global total

	if len(replacements) == pattern.count('?'):
			if is_valid(pattern + '.', replacements, nums): return 1
	
	if is_valid(pattern + '.', replacements, nums):
			return count(pattern, (*replacements, '.'), nums) + count(pattern, (*replacements, '#'), nums)
	return 0

for line in data:
	pattern, nums = line.split()
	nums = tuple(int(i) for i in nums.split(','))

	total += count(pattern, ('.',), nums)
	total += count(pattern, ('#',), nums)


print(total)
with open('in.txt') as f: data = [line.strip() for line in f.readlines()]
sum = 0

for line in data:
	nums = [[int(i) for i in line.split()]]
	count, length = 1, len(nums[0])
	while True:
		nums.append([])
		for i in range(1, length):
			nums[count].append(nums[count-1][i] - nums[count-1][i-1])
	
		length -= 1
		if set(nums[count]) == {0}: break
		count += 1

	nums, length = nums[::-1], len(nums)
	for i in range(1, length):
		nums[i].append(nums[i][-1] + nums[i-1][-1])
	sum += nums[-1][-1]

print(sum)
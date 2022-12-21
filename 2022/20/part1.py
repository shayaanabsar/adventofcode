with open('in.txt') as f:
	nums = []
	for i, num in enumerate(f.readlines()):
		nums.append((int(num), i))
	new_order = [(num, i) for (num, i) in nums]


length = len(nums)

def find_index(id):
	for i, val in enumerate(new_order):
		num, ix = val

		if ix == id:
			return i

for i, val in enumerate(nums):
	num, ix = val

	curr_index = find_index(ix)

	if num > 0:
		step = 1
	else:
		step = -1
	
	for j in range(abs(num) % (length - 1)):
		new_order[curr_index], new_order[(curr_index+step) % length] = new_order[(curr_index+step) % length], new_order[curr_index]
		curr_index = (curr_index+step) % length

for i, (num, id) in enumerate(new_order):
	if num == 0:
		zero_index = i
		break

coordinates = [1000, 2000, 3000]
total = 0

for coordinate in coordinates:
	total += new_order[(zero_index + coordinate) % length][0]

print(total)
from re import findall

with open('in.txt') as f: data = [line.strip() for line in f.readlines()]  + ['', '']
current_data, new_data = [int(i) for i in findall(r'\d+', data[0])], []


for i, line in enumerate(data[1:]):
	nums = [int(i) for i in findall(r'\d+', line)]

	if len(nums) == 0: 
		if new_data != []:
			new_data += list(set(current_data).difference(seen))
			current_data = new_data
		
		new_data, seen = [], set()
		continue

	conversion_start, original_start, length = nums
	start, end = original_start, original_start + length - 1
	
	for i, data in enumerate(current_data):
		if start <= data <= end:
			new_data.append((data - start) + conversion_start)
			seen.add(data)

print(min(current_data))
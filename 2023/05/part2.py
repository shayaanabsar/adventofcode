from re import findall
from copy import copy

with open('in.txt') as f: data = [line.strip() for line in f.readlines()]  + ['', '']
seeds, new_data, current_data = [int(i) for i in findall(r'\d+', data[0])], [], []

for i in range(0, len(seeds), 2): current_data.append((seeds[i], seeds[i]+seeds[i+1]))
ranges = []



for i, line in enumerate(data[1:]):
	nums = [int(i) for i in findall(r'\d+', line)]

	if len(nums) == 0:
		if i > 1:
			while current_data:
				start, end = current_data.pop()
				merged = False
				for conv_start, rule_start, length in ranges:
					rule_end = rule_start + length
					overlap_start, overlap_end = max(start, rule_start), min(end, rule_end)

					if overlap_start < overlap_end:
						new_data.append((overlap_start-rule_start+conv_start, overlap_end-rule_start+conv_start))

						if overlap_start > start:
							current_data.append((start, overlap_start))
						if overlap_end < end:
							current_data.append((overlap_end, end))
						merged = True
						break
				if not merged:
					new_data.append((start, end))

			ranges = []
			current_data = new_data
			new_data = []
		continue

	ranges.append(nums)

print(min(current_data, key=lambda x: x[0])[0])
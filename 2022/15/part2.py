import re

sensors_beacons = set()

MAX_ROWS = 4000000

def merge_ranges(ranges):
	ranges = sorted(ranges, key=lambda x: x[0])
	new_ranges = [ranges[0]]
	
	for range in ranges[1:]:
		previous_range = new_ranges[-1]
		start1, end1 = previous_range
		start2, end2 = range

		if start2 <= end1:
			new_ranges[-1] = (start1, max(end1, end2))
		else:
			new_ranges.append(range)
	return new_ranges
 
	
def check(row):
	ranges = []

	for sensor, beacon in sensors_beacons:
		manhattan_distance = abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1])
		diff = abs(row - sensor[1])
		
		if diff <= manhattan_distance:
			either_side = abs(diff-manhattan_distance)
			ranges.append((max(0, sensor[0]-either_side), min(MAX_ROWS, sensor[0]+either_side)))
	
	ranges = merge_ranges(ranges)
	pr_end = None

	for start, end in ranges:
		if pr_end is not None:
			if pr_end + 1 != start:
				return pr_end + 1
		pr_end = end

with open('in.txt', 'r') as file:
	data = file.readlines()

	for line in data:
		line = line.strip('\n')
		sensor, beacon = re.findall(r'x=(-?\d+), y=(-?\d+)', line)
		
		sensors_beacons.add((
			(int(sensor[0]), int(sensor[1])), (int(beacon[0]), int(beacon[1]))
		))
			
for i in range(MAX_ROWS):
	response = check(i)
	if response is not None:
		print(response * 4000000 + i)
		break

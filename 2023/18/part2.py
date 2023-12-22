from ast import literal_eval

with open('in.txt') as f: data = [line.strip().split() for line in f.readlines()]

mappings = {'3': (-1, 0), '0': (0, 1), '1': (1, 0), '2': (0, -1)}
points = [(0, 0)]
area, border = 0, 0

for line in data:
	distance, direction = literal_eval(f'0x{line[2][2:-2]}'), line[2][-2]
	diffs = (mappings[direction][0] * distance, mappings[direction][1] * distance)
	points.append((points[-1][0] + diffs[0], points[-1][1] + diffs[1]))
	border += distance
	area += (points[-1][0] + points[-2][0]) * (points[-1][1] - points[-2][1])
	
print(int(abs(border / 2) + abs(area / 2) + 1))

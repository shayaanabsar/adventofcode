with open('in.txt') as f: data = [line.strip().split() for line in f.readlines()]

mappings = {'U': (-1, 0), 'R': (0, 1), 'D': (1, 0), 'L': (0, -1)}
points = [(0, 0)]
area, border = 0, 0

for line in data:
	direction, distance, _ = line
	distance = int(distance)
	diffs = (mappings[direction][0] * distance, mappings[direction][1] * distance)
	points.append((points[-1][0] + diffs[0], points[-1][1] + diffs[1]))
	border += distance
	area += (points[-1][0] + points[-2][0]) * (points[-1][1] - points[-2][1])


print(int(abs(border / 2) + abs(area / 2) + 1))
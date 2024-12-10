from collections import defaultdict

with open('in.txt') as f: data = [line.strip() for line in f.readlines()]

def validate_twice_distance(a1, a2, p):
    # Check if dist(p, a2) == 2 * dist(p, a1)
    d1 = (p[0] - a1[0])**2 + (p[1] - a1[1])**2
    d2 = (p[0] - a2[0])**2 + (p[1] - a2[1])**2
    return d2 == 4 * d1

locations = defaultdict(lambda : [])

for i, r in enumerate(data):
	for j, c in enumerate(r):
		if c != '.': locations[c].append((i, j))

act = set()

for freq in locations:
	for a1 in locations[freq]:
		for a2 in locations[freq]:
			if a1 == a2: continue

			i_diff, j_diff = a1[0] - a2[0], a1[1] - a2[1]
			y_1, x_1 = a1


			g = i_diff / j_diff
			# line: y - y_1 = g*x - g*x_1 -> y = g*x - g*x_1 + y_1

			for x in range(len(data[0])):
				y = g * (x - x_1) + y_1

				if y % 1 == 0 and 0 <= y < len(data):
					act.add((y, x))

print(len(act))
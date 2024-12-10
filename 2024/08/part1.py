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


			antinodes = [(a2[0] + 2 * i_diff, a2[1] + 2 * j_diff), 
						 (a2[0] - 2 * i_diff, a2[1] - 2 * j_diff)]
			
			for (i, j) in antinodes:
				if 0 <= i < len(data) and 0 <= j < len(data[0]):
					if validate_twice_distance(a1, a2, (i, j)):
						act.add((i, j))

print(len(act))

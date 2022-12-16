import re

sensors_beacons = set()
not_allowed = set()

row = 2000000

def fill(sensor, beacon):
	global row
	
	manhattan_distance = abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1])
	cnt = manhattan_distance

	if sensor[1]-manhattan_distance-1 < row <= sensor[1]:
		cnt -= (abs(sensor[1] - row))
		for x in range(sensor[0]-cnt, sensor[0]+cnt+1):
			if (x, row) not in sensors_beacons:
				not_allowed.add((x, row))

	
	cnt = manhattan_distance

	if sensor[1] <= row < sensor[1]+manhattan_distance+1:
		cnt -= (abs(sensor[1] - row))
		for x in range(sensor[0]-cnt, sensor[0]+cnt+1):
			if (x, row) not in sensors_beacons:
				not_allowed.add((x, row))

with open('in.txt', 'r') as file:
	data = file.readlines()

	for line in data:
		line = line.strip('\n')
		sensor, beacon = re.findall(r'x=(-?\d+), y=(-?\d+)', line)
		
		sensors_beacons.add((int(sensor[0]), int(sensor[1])))
		sensors_beacons.add((int(beacon[0]), int(beacon[1])))
			
		fill((int(sensor[0]), int(sensor[1])), (int(beacon[0]), int(beacon[1])))

print(len(not_allowed))
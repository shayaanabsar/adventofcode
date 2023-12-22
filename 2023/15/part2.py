from re import findall

with open('in.txt') as f: data = f.read().split(',')

boxes = [[] for _ in range(256)]

def hash(word):
	current_total = 0
	for c in word:
		current_total += ord(c)
		current_total *= 17
		current_total %= 256
	return current_total

def handle(box, label, num=None):
	for i, v in enumerate(boxes[box]):
		l, _ = v
		if l  == label: 
			if num is None: boxes[box] = boxes[box][:i] + boxes[box][i+1:]
			else: boxes[box][i] = (label, num)
			return
	if num is not None: boxes[box].append((label, num))



for instr in data:
	label, op, num = findall(r'([a-z]+)(-|=)(\d*)', instr)[0]
	box = hash(label)
	if op == '-': handle(box, label)
	else: handle(box, label, int(num))


total  = 0
for i, box in enumerate(boxes):
	for j, lens in enumerate(box):
		total += ((i + 1) * (j + 1) * lens[1])

print(total)


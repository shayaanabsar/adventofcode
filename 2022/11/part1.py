from math import floor
from collections import deque

monkeys = []

class Monkey:
	def __init__(self):
		self.items = None
		self.operation = None
		self.test = None
		self.true = None
		self.false = None
		self.inspect_count = 0
	
	def turn(self):
		for item in self.items:
			old = item
			worry_level = eval(f'item {self.operation}')
			worry_level /= 3
			worry_level = floor(worry_level)

			if worry_level % self.test == 0:
				monkeys[self.true].items.append(worry_level)
			else:
				monkeys[self.false].items.append(worry_level)
			
			self.inspect_count += 1
		self.items = deque()


with open('in.txt', 'r') as file:
	data = file.readlines()

for line in data:
	line = line.strip()
	
	if line[:7] == 'Monkey ':
		monkeys.append(Monkey())
	elif line[:16] == 'Starting items: ':
		monkeys[-1].items = deque(int(i) for i in line[16:].split(','))
	elif line[:21] == 'Operation: new = old ':
		monkeys[-1].operation = line[21:]
	elif line[:19] == 'Test: divisible by ':
		monkeys[-1].test = int(line[19:])
	elif line[:25] == 'If true: throw to monkey ':
		monkeys[-1].true = int(line[25:])
	elif line[:26] == 'If false: throw to monkey ':
		monkeys[-1].false = int(line[26:])

for i in range(20):
	for j in range(len(monkeys)):
		monkeys[j].turn()

monkeys = sorted(monkeys, key=lambda x: x.inspect_count, reverse=True)
print(monkeys[0].inspect_count * monkeys[1].inspect_count)
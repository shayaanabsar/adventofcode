from re import finditer
from collections import deque

with open('in.txt') as f: data = [line.strip() for line in f.readlines()]

score = 0

scores = {}

for line in data:
	numbers, sep = finditer(r'\d+', line), line.index('|')
	
	winning_numbers, matches  = set(), 0

	card_number = None

	for number in numbers:
		if card_number is None:
			card_number = int(number.group())
			continue
		index, num = number.start(), int(number.group())

		if index < sep:
			winning_numbers.add(num)
		elif num in winning_numbers:
			matches += 1
	
	scores[card_number] = matches

queue = deque([i for i in range(1, len(scores) + 1)])
score = 0

while queue:
	curr = queue.popleft()
	for i in range(curr+1, curr+scores[curr]+1): queue.appendleft(i)
	score += 1

print(score)


from re import finditer
from functools import lru_cache

with open('in.txt') as f: data = [line.strip() for line in f.readlines()]

scores = {}

for line in data:
	numbers, sep = [(i.start(), int(i.group())) for i in finditer(r'\d+', line)], line.index('|')
	card_number, numbers = numbers[0][1], numbers[1:]
	
	winning_numbers     = {j for i, j in numbers if i < sep}
	scratchcard_numbers = {j for i, j in numbers if i > sep}

	scores[card_number] = len(winning_numbers.intersection(scratchcard_numbers))


@lru_cache
def calc_score(card_number):
	score = 1
	for i in range(card_number+1, card_number+scores[card_number]+1): score += calc_score(i)
	return score

score = 0
for i in range(1, len(scores)+1): score += calc_score(i)
print(score)
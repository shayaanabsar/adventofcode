from re import finditer
from functools import lru_cache

with open('in.txt') as f: data = [line.strip() for line in f.readlines()]

score, scores = 0, {}

for line in data:
	numbers, sep = finditer(r'\d+', line), line.index('|')
	
	winning_numbers, matches, card_number  = set(), 0, None

	for number in numbers:
		index, num = number.start(), int(number.group())

		if card_number is None:
			card_number = num
			continue

		if index < sep:
			winning_numbers.add(num)
		elif num in winning_numbers:
			matches += 1
	
	scores[card_number] = matches


@lru_cache
def calc_score(card_number):
	score = 1
	for i in range(card_number+1, card_number+scores[card_number]+1): score += calc_score(i)
	return score

score = 0
for i in range(1, len(scores)+1): score += calc_score(i)
print(score)
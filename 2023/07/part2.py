import collections

with open('in.txt') as f: 
	hands = []
	for line in f.readlines():
		hand, val = line.strip().split()
		js = {i for i, v in enumerate(hand) if v == 'J'}
		most_common = collections.Counter(hand).most_common() + [('K', 0)]
		most_common = most_common[1][0] if most_common[0][0] == 'J' else most_common[0][0]
		hand = hand.replace('J', most_common)
		hands.append((hand, int(val), js))

labels = 'AKQT98765432'

def hand_type(hand):
	kinds = set(hand)

	if len(kinds) == 1: return 0
	elif len(kinds) == 2:
		for kind in kinds:
			if hand.count(kind) == 4: return 1
		return 2
	elif len(kinds) == 3:
		for kind in kinds:
			if hand.count(kind) == 3: return 3
		return 4
	elif len(kinds) == 4: return 5
	return 6


def is_greater(hand1, hand2):
	js1, js2 = hand1[2], hand2[2]
	hand1, hand2 = hand1[0], hand2[0]
	type_1, type_2 = hand_type(hand1), hand_type(hand2)

	if type_1 < type_2: return True
	elif type_1 > type_2: return False

	for i, label1 in enumerate(hand1):
		if i in js1: level1 = 100
		else: level1 = labels.index(label1)

		if i in js2: level2 = 100
		else: level2 = labels.index(hand2[i])

		if level1 < level2:
			return True
		elif level1 > level2:
			return False
	return 0

for i, val in enumerate(hands):
	pos = i
	while pos > 0 and is_greater(hands[pos-1], val):
		hands[pos] = hands[pos-1]
		pos -= 1
	hands[pos] = val

winnings = 0


for i, hand in enumerate(hands):
	winnings += (i+1) * hand[1]

print(winnings)
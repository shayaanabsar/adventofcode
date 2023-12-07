with open('in.txt') as f: 
	hands = []
	for line in f.readlines():
		hand, val = line.strip().split()
		hands.append((hand, int(val)))

labels = 'AKQJT98765432'

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
	type_1, type_2 = hand_type(hand1), hand_type(hand2)

	if type_1 < type_2: return True
	elif type_1 > type_2: return False

	for i, label1 in enumerate(hand1):
		if labels.index(label1) < labels.index(hand2[i]):
			return True
		elif labels.index(label1) > labels.index(hand2[i]):
			return False
	return 0

for i, val in enumerate(hands):
	pos = i
	while pos > 0 and is_greater(hands[pos-1][0], val[0]):
		hands[pos] = hands[pos-1]
		pos -= 1
	hands[pos] = val

winnings = 0


for i, hand in enumerate(hands):
	winnings += (i+1) * hand[1]

print(winnings)
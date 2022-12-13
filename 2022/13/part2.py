from ast import literal_eval

with open('in.txt') as f:
	data = f.readlines()
	packets = []
	for i in range(len(data)):
		if data[i] != '\n':
			packets.append(literal_eval(data[i].strip('\n')))

IN_ORDER = 0
OUT_OF_ORDER = 1
CONTINUE_CHECKING = 2

def test_packets(p1, p2):
	for i in range(len(p1)):
		if i >= len(p2):
			return OUT_OF_ORDER
		a = p1[i]
		b = p2[i]

		if type(a) == type(b) == int:
			if a > b:
				return OUT_OF_ORDER
			elif a < b:
				return IN_ORDER
		elif type(a) == type(b) == list:
			response = test_packets(a, b)
			if response != CONTINUE_CHECKING:
				return response
		else:
			if type(a) == int:
				a = [a]
			else:
				b = [b]

			response = test_packets(a, b)

			if response != CONTINUE_CHECKING:
				return response

	if len(p1) < len(p2):
		return IN_ORDER

	return CONTINUE_CHECKING

packets.append([[2]])
packets.append([[6]])

for i in range(len(packets) - 1):
	for j in range(len(packets) - 1):
		if test_packets(packets[j], packets[j+1]) != IN_ORDER:
			packets[j], packets[j+1] = packets[j+1], packets[j]

print((packets.index([[2]]) + 1) * (packets.index([[6]]) + 1))
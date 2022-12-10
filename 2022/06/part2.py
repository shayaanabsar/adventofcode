with open('in.txt', 'r') as file:
	s = file.readline()

for i in range(len(s)-14):
	if len(set(s[i:i+14])) == len(s[i:i+14]):
		print(i+14)
		break

with open('in.txt', 'r') as file:
	s = file.readline()

for i in range(len(s)-4):
	if len(set(s[i:i+4])) == len(s[i:i+4]):
		print(i+4)
		break

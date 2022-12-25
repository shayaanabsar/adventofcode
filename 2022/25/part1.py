digits = {
		'=': -2,
		'-': -1,
		'0': 0,
		'1': 1,
		'2': 2 
}

with open('in.txt') as f:
	total = 0

	for num in f.readlines():
		num = num.strip('\n')[::-1]
		converted_num = 0

		for i, digit in enumerate(num):
			converted_num += ((5 ** i) * digits[digit])
		total += converted_num

converted_num = ''
carry = 0

digits = {digits[value]:value for value in digits}

while total > 0:
	res = (total % 5) + carry

	if res > 2:
		res -= 5
		carry = 1
	else:
		carry = 0
	
	converted_num = digits[res] + converted_num
	total //= 5

print(converted_num)
	
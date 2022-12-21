from copy import deepcopy

vals = {}
formulae = {}

with open('in.txt') as f:
	for line in f.readlines():
		words=line.strip('\n').split()
		if len(words) == 2:
			vals[words[0][:-1]] = words[1].strip()
		else:
			formulae[words[0][:-1]] = words[1:]
	vals['humn'] = 'h'

def evaluate(name):
	if name in vals:
		return vals[name]
	elif name in formulae:
		left, symbol, right = formulae[name]
		if name == 'root':
			return (evaluate(left), evaluate(right))
		match symbol:
			case '+':
				vals[name] = f'({evaluate(left)} + {evaluate(right)})'
			case '-': 
				vals[name] = f'({evaluate(left)} - {evaluate(right)})'
			case '*': 
				vals[name] = f'({evaluate(left)} * {evaluate(right)})'
			case '/':
				vals[name] = f'({evaluate(left)} / {evaluate(right)})'

		return vals[name]

left, right = evaluate('root')

try:
	equation = f'{left} = {eval(right)}'
except NameError:
	equation = f'{right} = {eval(left)}'

with open('equation.txt', 'w+') as f:
	f.write(equation)

# Plug equation into MathPapa to get answer
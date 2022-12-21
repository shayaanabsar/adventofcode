vals = {}
formulae = {}

with open('in.txt') as f:
	for line in f.readlines():
		words=line.strip('\n').split()
		
		if len(words) == 2:
			vals[words[0][:-1]] = int(words[1])
		else:
			formulae[words[0][:-1]] = words[1:]

root_formula = formulae['root']

def evaluate(name):
	if name in vals:
		return vals[name]
	elif name in formulae:
		left, symbol, right = formulae[name]
		
		match symbol:
			case '+':
				vals[name] = evaluate(left) + evaluate(right)
			case '-': 
				vals[name] = evaluate(left) - evaluate(right)
			case '*': 
				vals[name] = evaluate(left) * evaluate(right)
			case '/':
				vals[name] = evaluate(left) / evaluate(right)

		return vals[name]
print(evaluate('root'))
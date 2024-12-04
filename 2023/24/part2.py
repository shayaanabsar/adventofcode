
from re import findall
from sympy import symbols
from sympy import solve

with open('in.txt') as f: data = [line.strip() for line in f.readlines()]

for i, line in enumerate(data):
	data[i] = [int(i) for i in findall(r'-*\d+', line)]	
	data[i] = [data[i][:3], data[i][3:]]

count = 0
intersections = set()

a, b, c, d, e, f = symbols('a'), symbols('b'), symbols('c'), symbols('d'), symbols('e'), symbols('f')
equations = []

for i in range(5):
	position_vector, direction_vector = data[i][0], data[i][1]
	alpha, beta, gamma  = position_vector
	delta, epsilon, phi = direction_vector

	equations.append((d-alpha)*(epsilon-b)-(delta-a)*(e-beta))
	equations.append((e-beta)*(phi-c)-(f-gamma)*(epsilon-b))

solutions = solve(equations)[0]
print(solutions[d]+solutions[e]+solutions[f])

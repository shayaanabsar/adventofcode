with open('in.txt') as f:  x, y = zip(*[[int(x) for x in line.strip().split()] for line in f.readlines()])
x, y = sorted(list(x)), sorted(list(y))
print(sum([abs(x[i] - y[i]) for i in range(len(x))]))
with open('in.txt') as f:  x, y = zip(*[[int(x) for x in line.strip().split()] for line in f.readlines()])
x, y = sorted(list(x)), sorted(list(y))
print(sum([(x[i] * y.count(x[i])) for i in range(len(x))]))
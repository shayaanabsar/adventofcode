from re import findall
from math import sqrt, ceil

with open('in.txt') as f: data = [line.strip() for line in f.readlines()]

time      = int(''.join([i for i in findall(r'\d+', data[0])]))
distance  =  int(''.join([i for i in findall(r'\d+', data[1])]))

root1 = ceil((time + sqrt(time ** 2 - 4 * distance)) / 2)
root2 = ceil((time - sqrt(time ** 2 - 4 * distance)) / 2)

print(abs(root2 - root1))
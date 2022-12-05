with open('in.txt', 'r') as file:
    data = file.readlines()

piles = [
    ['S', 'P', 'W', 'N', 'J', 'Z'],
    ['T', 'S', 'G'],
    ['H', 'L', 'R', 'Q', 'V'],
    ['D', 'T', 'S', 'V'],
    ['J', 'M', 'B', 'D', 'T', 'Z', 'Q'],
    ['L', 'Z', 'C', 'D', 'J', 'T', 'W', 'M'],
    ['J', 'T', 'G', 'W', 'M', 'P', 'L'],
    ['H', 'Q', 'F', 'B', 'T', 'M', 'G', 'N'],
    ['W', 'Q', 'B', 'P', 'C', 'G', 'D', 'R']
]


for line in data:
    line = line.strip('\n').split(' ')
    start, end, amount = int(line[3])-1, int(line[5])-1, int(line[1])

    buffer = piles[start][:amount]
    piles[start] = piles[start][amount:]
    piles[end] = buffer + piles[end]
    
for i, v in enumerate(piles):
    print(v[0], end='')
print('')
import string

with open('in.txt', 'r') as file:
    data = file.readlines()


alphabet = string.ascii_lowercase
priority = 0

for i in range(0, len(data), 3):
    group = []

    for j in range(i, i+3):
        group.append(data[j].strip('\n'))
    
    for char in group[0]:
        if char in group[1] and char in group[2]:
            break

    priority += alphabet.index(char.lower()) + 1

    if char.isupper():
        priority += 26
    
print(priority)

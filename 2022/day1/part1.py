with open('in.txt', 'r') as file:
    data = file.readlines()
    amounts = []
    curr = 0

    for line in data:
        if line == '\n':
            amounts.append(curr)
            curr = 0
        else:
            line = line.strip('\n')
            curr += int(line)
    print(max(amounts))

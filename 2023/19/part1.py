from re import findall
with open('in.txt') as f: data = [line.strip() for line in f.readlines()]

workflows = {}
seen = False
total = 0

def parse_workflow(line):
	name, conditions = line[0], line[1:]
	workflow = []
	for i in range(0, len(conditions), 3):
		try:
			sign, num = conditions[i+1][0], int(conditions[i+1][1:])
			workflow.append((conditions[i], sign, num, conditions[i+2]))
		except IndexError: workflow.append((conditions[i],))
	workflows[name] = workflow

def solve(curr_workflow, props):
	if curr_workflow == 'A': return sum(props.values())
	if curr_workflow == 'R': return 0

	for rule in workflows[curr_workflow]:
		if len(rule) == 1: return solve(rule[0], props)
		else:
			p, sign, num, new_workflow = rule

			if sign == '>' and props[p] > num: return solve(new_workflow, props)
			elif sign == '<' and props[p] < num: return solve(new_workflow, props)

	
for line in data:
	if line == '': 
		seen = True
		continue
	line = findall(r'[<>]*\w+', line)

	if not seen:
		parse_workflow(line)
	else:
		props = {line[i]:int(line[i+1]) for i in range(0, len(line)-1, 2)}
		total += solve('in', props)

print(total)		


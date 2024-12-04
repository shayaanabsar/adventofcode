from re import findall
import numpy as np

with open('in.txt') as f: data = [line.strip() for line in f.readlines()]

for i, line in enumerate(data):
	data[i] = [int(i) for i in findall(r'-*\d+', line)]	
	data[i] = [data[i][:2], data[i][3:-1]]

count = 0

for i, equation1 in enumerate(data):
	for equation2 in data[:i]:
		position_vector_1, direction_vector_1 = equation1
		position_vector_2, direction_vector_2 = equation2

		coefficients = np.matrix([[direction_vector_1[0], -direction_vector_2[0]], [direction_vector_1[1], -direction_vector_2[1]]])
		sums         = np.matrix([[position_vector_2[0]-position_vector_1[0]], [position_vector_2[1]-position_vector_1[1]]])

		try:
			answer = np.matmul(np.linalg.inv(coefficients), sums)
		except np.linalg.LinAlgError: continue

		alpha, beta = answer.item((0, 0)), answer.item((1, 0))

		x = position_vector_1[0] + alpha * direction_vector_1[0]
		y = position_vector_1[1] + alpha * direction_vector_1[1]

		if 200000000000000 <= x <= 400000000000000 and 200000000000000 <= y <= 400000000000000 and alpha >= 0 and beta >= 0: count += 1

print(count)
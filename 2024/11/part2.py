from functools import lru_cache

with open('in.txt') as f: stones = [int(i) for i in f.readline().split()]

@lru_cache(maxsize=None)
def sim_stone(val, t):
	if t == 75: return 1
	length, str_s = len(str(val)), str(val)
	if val == 0: return sim_stone(1, t+1)
	elif length % 2 == 0:
		l, r = int(str_s[:length // 2]), int(str_s[length // 2:])
		return sim_stone(l, t+1) + sim_stone(r, t+1)
	else:
		return sim_stone (val * 2024, t+1)

num = 0

for s in stones:
	num += sim_stone(s, 0)
print(num)
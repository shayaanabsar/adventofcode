import os
import time

print("""
🎄🎅✨🎁🔔🦌🤶⛄❄️🕯️ Advent of Code! 🕯️❄️⛄🤶🦌🔔🎁✨🎅🎄
""")

year = input("📅 Enter the year: ")
day  = input("🎁 Enter the day: ").zfill(2)

def create_file(name, year, day):
	with open(f'{year}/{day}/{name}', 'w+'):
		return

def create_day(year, day):
	os.mkdir(f'{year}/{day}')
	create_file('part1.py', year, day)
	create_file('part2.py', year, day)
	create_file('in.txt', year, day)

def run_and_measure_time(year, day, part):
	print(f'\nPart {part}: \u001b[32m', end='')
	start = time.time()
	os.system(f'cd {year}/{day}; python3 part{part}.py')
	end = time.time()
	print(f'\u001b[31m{end - start:.4f} seconds\u001b[0m')


try:
	open(f'{year}/{day}/part1.py', 'r')
except FileNotFoundError:
	create_day(year, day)
	print('\u001b[32mSuccessfully created day.\u001b[0m')
else:
	run_and_measure_time(year, day, '1')
	run_and_measure_time(year, day, '2')
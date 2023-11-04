import os
import time

print("""
🎄🎅✨🎁🔔🦌🤶⛄❄️🕯️ Advent of Code! 🕯️❄️⛄🤶🦌🔔🎁✨🎅🎄
""")

year = input("📅 Enter the year: ")
day = input("🎁 Enter the day: ").zfill(2)

def run_and_measure_time(year, day, part):
	try:
		print(f'\nPart {part} -')
		start = time.time()
		os.system(f'cd {year}/{day}; python3 part{part}.py')
		end = time.time()
		print(f'{end - start:.4f} seconds\n')
	except FileExistsError:
		print('File doesn\'t exist')

run_and_measure_time(year, day, '1')
run_and_measure_time(year, day, '2')
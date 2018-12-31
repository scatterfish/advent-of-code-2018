#!/usr/bin/env python3

from math import floor
from multiprocessing import Pool

SEARCH_SIZE = 20 # how many sizes to brute force, answers always seem to be < 20
THREAD_COUNT = 8

serial_num = 0
grid = [[0] * 300 for row in range(300)]

def main():
	global serial_num
	global grid
	
	with open("input.txt") as input_file:
		serial_num = int(input_file.read().strip())
	
	for x in range(0, 300):
		for y in range(0, 300):
			grid[x][y] = get_power_level(x, y)
	
	x_1, y_1, s_1, p_1 = calculate_power_data(3)
	
	p = Pool(processes=THREAD_COUNT)
	results = p.map(calculate_power_data, range(1, SEARCH_SIZE))
	
	x_2 = 0
	y_2 = 0
	size = 0
	max_power = 0
	for x, y, s, p in results:
		if p > max_power:
			max_power = p
			x_2 = x
			y_2 = y
			size = s
	
	print("Part 1 answer: %d,%d" % (x_1, y_1))
	print("Part 2 answer: %d,%d,%d" % (x_2, y_2, size))
	

def calculate_power_data(size):
	print("Size %d starting..." % size)
	max_power = 0
	x_coord = 0
	y_coord = 0
	for x in range(0, 300 - size + 1):
		for y in range(0, 300 - size + 1):
			power_level = 0
			for box_x in range(0, size):
				for box_y in range(0, size):
					power_level += grid[x + box_x][y + box_y]
			if power_level > max_power:
				max_power = power_level
				x_coord = x + 1
				y_coord = y + 1
	print("Size %d done" % size)
	return (x_coord, y_coord, size, max_power)

def get_power_level(x, y):
	rack_id = (x + 1) + 10
	return floor(((((rack_id * (y + 1)) + serial_num) * rack_id) / 100) % 10) - 5

if __name__ == "__main__":
	main()

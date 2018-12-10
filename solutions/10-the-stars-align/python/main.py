#!/usr/bin/env python3

class Particle:
	def __init__(self, x_pos, y_pos, x_vel, y_vel):
		self.x_pos = x_pos
		self.y_pos = y_pos
		self.x_vel = x_vel
		self.y_vel = y_vel

def main():
	
	with open("input.txt") as input_file:
		lines = input_file.read().strip().split("\n")
	
	particles = []
	for line in lines:
		x_pos = int(line[10:16])
		y_pos = int(line[17:24])
		x_vel = int(line[36:38])
		y_vel = int(line[39:42])
		particles.append(Particle(x_pos, y_pos, x_vel, y_vel))
	
	min_size = 1000000
	time = 0
	for i in range(0, 1000000):
		x_pos_list = [p.x_pos + (p.x_vel * i) for p in particles]
		y_pos_list = [p.y_pos + (p.y_vel * i) for p in particles]
		x_min, x_max = minmax(x_pos_list)
		y_min, y_max = minmax(y_pos_list)
		size = (x_max - x_min) + (y_max - y_min)
		if size < min_size:
			min_size = size
			time = i
		else:
			break
	
	x_pos_list = [p.x_pos + (p.x_vel * time) for p in particles]
	y_pos_list = [p.y_pos + (p.y_vel * time) for p in particles]
	x_min, x_max = minmax(x_pos_list)
	y_min, y_max = minmax(y_pos_list)
	
	grid = [[" "] * (x_max - x_min + 1) for row in range(y_max - y_min + 1)]
	
	for x, y in zip(x_pos_list, y_pos_list):
		grid[y - y_min][x - x_min] = "█"
	
	for row in grid:
		print("".join(row))
	
	print("Answer found at time %d" % time)
	

def minmax(arr):
	return min(arr), max(arr)

if __name__ == "__main__":
	main()

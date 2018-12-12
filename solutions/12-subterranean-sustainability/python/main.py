#!/usr/bin/env python3

GEN_MAX = 200 # max generation to compute sum for, should be stablized ~200
MARGIN_SCALE = 5 # how much to increase the list margins each iteration

def main():
	
	with open("input.txt") as input_file:
		lines = input_file.read().strip().split("\n")
	
	plants = [p == "#" for p in lines[0][15:]]
	
	margin = add_plant_margin(plants, 0)
	
	growth_map = {}
	for i in range(2, len(lines)):
		pattern, result = lines[i].split(" => ")
		growth_map[pattern] = result
	
	print("Calculating...")
	
	gen_20_sum = 0
	penultimate_sum = 0
	last_sum = 0
	for gen in range(0, GEN_MAX):
		if gen == 20:
			gen_20_sum = get_plant_sum(plants, margin)
		elif gen == GEN_MAX - 2:
			penultimate_sum = get_plant_sum(plants, margin)
		elif gen == GEN_MAX - 1:
			last_sum = get_plant_sum(plants, margin)
		plants_next = plants.copy()
		for plant_index in range(0, len(plants_next) - 5):
			group = [False] * 5
			for group_index in range(0, 5):
				group[group_index] = plants[plant_index + group_index]
			group_str = get_plant_str(group)
			if group_str in growth_map:
				plants_next[plant_index + 2] = growth_map[group_str] == "#"
		margin = add_plant_margin(plants_next, margin)
		plants = plants_next
	
	stable_diff = last_sum - penultimate_sum
	
	print("Part 1 answer: %d" % gen_20_sum)
	print("Part 2 answer: %d" % ((last_sum + stable_diff) + stable_diff * (50000000000 - GEN_MAX)))
	

def add_plant_margin(plants, prev_margin):
	for _ in range(0, MARGIN_SCALE): # faster to do all insertions first
		plants.insert(0, False)
	for _ in range(0, MARGIN_SCALE):
		plants.append(False)
	return prev_margin + MARGIN_SCALE

def get_plant_str(plants):
	return "".join(["#" if p == True else "." for p in plants])

def get_plant_sum(plants, margin):
	plant_sum = 0
	for i in range(0, len(plants)):
		if plants[i]:
			plant_sum += i - margin
	return plant_sum
	

if __name__ == "__main__":
	main()

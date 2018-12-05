#!/usr/bin/env python3

class Claim:
	def __init__(self, claim_id, margin_left, width, margin_top, height):
		self.claim_id = claim_id
		self.width_lower = margin_left
		self.width_upper = margin_left + width
		self.height_lower = margin_top
		self.height_upper = margin_top + height

def main():
	
	with open("input.txt") as input_file:
		lines = input_file.read().strip().split("\n")
	
	claim_list = []
	for l in lines:
		claim_id    = int(l[l.find("#") + 1:l.find("@")])
		margin_left = int(l[l.find("@") + 1:l.find(",")])
		margin_top  = int(l[l.find(",") + 1:l.find(":")])
		width       = int(l[l.find(":") + 1:l.find("x")])
		height      = int(l[l.find("x") + 1:])
		claim_list.append(Claim(claim_id, margin_left, width, margin_top, height))
	
	grid = []
	for x in range(0, 1000):
		row = []
		for y in range(0, 1000):
			row.append(0)
		grid.append(row)
	
	for claim in claim_list:
		for x in range(claim.width_lower, claim.width_upper):
			for y in range(claim.height_lower, claim.height_upper):
				grid[x][y] += 1
	
	overlap_count = 0
	for x in range(0, 1000):
		for y in range(0, 1000):
			if grid[x][y] > 1:
				overlap_count += 1
	
	print("Overlapping tiles: %d" % overlap_count)
	
	for claim in claim_list:
		is_valid = True
		for x in range(claim.width_lower, claim.width_upper):
			for y in range(claim.height_lower, claim.height_upper):
				if grid[x][y] > 1:
					is_valid = False
		if is_valid:
			print("Valid claim: %d" % claim.claim_id)
			break

if __name__ == "__main__":
	main()

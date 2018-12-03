#!/usr/bin/env python

import sys

class Claim:
	def __init__(self, claim_id, margin_left, width, margin_top, height):
		self.claim_id = claim_id
		self.margin_left = margin_left
		self.width = width
		self.margin_top = margin_top
		self.height = height

def main():
	
	with open("input.txt") as fp:
		lines = fp.read().strip().split("\n")
	
	grid = []
	for i in range(0, 1000):
		row = []
		for k in range(0, 1000):
			row.append(0)
		grid.append(row)
	
	claim_list = []
	for claim in lines:
		pieces = claim.split()
		claim_id = int(pieces[0].replace("#", ""))
		margin_data = pieces[2].replace(":", "").split(",")
		margin = [int(margin_data[0]), int(margin_data[1])]
		measure_data = pieces[3].split("x")
		measure = [int(measure_data[0]), int(measure_data[1])] 
		claim_list.append(Claim(claim_id, margin[0], measure[0], margin[1], measure[1]))
	
	for claim in claim_list:
		for i in range(claim.margin_left, claim.margin_left + claim.width):
			for k in range(claim.margin_top, claim.margin_top + claim.height):
				grid[i][k] += 1
	
	overlap_count = 0
	for i in range(0, 1000):
		for k in range(0, 1000):
			if grid[i][k] > 1:
				overlap_count += 1
	
	print("Overlapping tiles: %d" % overlap_count)
	
	for claim in claim_list:
		is_valid = True
		for i in range(claim.margin_left, claim.margin_left + claim.width):
			for k in range(claim.margin_top, claim.margin_top + claim.height):
				if grid[i][k] > 1:
					is_valid = False
		if is_valid:
			print("Valid claim: %d" % claim.claim_id)
			sys.exit(0)

if __name__ == "__main__":
	main()

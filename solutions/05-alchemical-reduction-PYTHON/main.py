#!/usr/bin/env python3

import os
import sys

def main():
	
	with open("input.txt") as input_file:
		chain = list(input_file.read().strip())
	
	print("Reacting polymer chain...")
	chain = react_polymer_chain(chain)
	print("Units left after reaction: %d" % len(chain))
	
	print("Testing polymer shrinks...")
	print("Minimum polymer length: %d" % get_min_length(chain))
	

def react_polymer_chain(chain):
	fully_reacted = False
	while not fully_reacted:
		had_reaction = False
		units_to_remove = []
		for i in range(0, len(chain) - 1):
			current_unit = chain[i]
			next_unit = chain[i + 1]
			if current_unit == next_unit:
				continue
			if current_unit.lower() == next_unit or current_unit.upper() == next_unit:
				if not i in units_to_remove:
					units_to_remove.append(i)
					units_to_remove.append(i + 1)
				had_reaction = True
		if had_reaction:
			for u in reversed(units_to_remove):
				del chain[u]
		else:
			fully_reacted = True
	return chain

def get_min_length(chain):
	min_length = len(chain)
	for u in list("abcdefghijklmnopqrstuvwxyz"):
		chain_shrink = [c for c in chain if c != u and c != u.upper()]
		chain_shrink = react_polymer_chain(chain_shrink)
		shrink_len = len(chain_shrink)
		if shrink_len < min_length:
			min_length = shrink_len
	return min_length

if __name__ == "__main__":
	try:
		main()
	except KeyboardInterrupt:
		print("\nKeyboard interrupt received. Exiting...")
		try:
			sys.exit(0)
		except SystemExit:
			os._exit(0)

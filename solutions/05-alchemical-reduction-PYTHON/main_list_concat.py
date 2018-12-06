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
	i = 0
	while i < len(chain) - 1:
		if chain[i] != chain[i + 1] and chain[i].lower() == chain[i + 1].lower():
			chain = chain[:i] + chain[i + 2:]
			if i != 0:
				i -= 1
		else:
			i += 1
	return chain

def get_min_length(chain):
	min_length = len(chain)
	for u in list("abcdefghijklmnopqrstuvwxyz"):
		chain_shrink = [c for c in chain if c != u and c != u.upper()]
		chain_shrink = react_polymer_chain(chain_shrink)
		min_length = min(min_length, len(chain_shrink))
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

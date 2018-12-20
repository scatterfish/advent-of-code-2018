#!/usr/bin/env python3

from itertools import cycle

def main():
	
	with open("input.txt") as input_file:
		frequency_deltas = [int(n) for n in input_file.read().strip().split("\n")]
	
	print("Calibration frequency: %d" % sum(frequency_deltas))
	
	frequency_sum = 0
	known_frequencies = set()
	for delta in cycle(frequency_deltas):
		frequency_sum += delta
		if frequency_sum in known_frequencies:
			print("First repeat frequency: %d" % frequency_sum)
			break
		known_frequencies.add(frequency_sum)
	

if __name__ == "__main__":
	main()

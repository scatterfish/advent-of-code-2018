#!/usr/bin/env python3

import os
import sys

def main():
	
	frequency_deltas = []
	frequency_sum = 0
	known_frequencies = []
	first_repeat = 0
	
	with open("input.txt") as input_file:
		line = input_file.readline().strip()
		while line:
			if line[0:1] == "+":
				delta = int(line[1:])
			else:
				delta = -int(line[1:])
			frequency_deltas.append(delta)
			line = input_file.readline().strip()
	
	print("Calculating... Be patient, this may take a while...")
	
	found_repeat = False
	first_loop = True
	while not found_repeat:
		for i in frequency_deltas:
			frequency_sum += i
			if frequency_sum in known_frequencies:
				first_repeat = frequency_sum
				found_repeat = True
				break
			known_frequencies.append(frequency_sum)
		if first_loop:
			print("Calibration: %s" % frequency_sum)
			first_loop = False
	
	print("First repeat frequency: %s" % first_repeat)

if __name__ == "__main__":
	try:
		main()
	except KeyboardInterrupt:
		print("\nKeyboard interrupt received. Exiting...")
		try:
			sys.exit(0)
		except SystemExit:
			os._exit(0)

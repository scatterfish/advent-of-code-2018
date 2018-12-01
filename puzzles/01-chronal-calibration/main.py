#!/bin/python

def main():
	
	frequency_sum = 0
	known_frequencies = []
	first_repeat = 0
	
	print("Calculating... Be patient, this may take a while...")
	
	first_pass = True
	found_repeat = False
	while not found_repeat:
		
		with open("input.txt") as fp:
			line = fp.readline().strip()
			while line:
				
				delta = int(line[1:])
				if line[0:1] == "+":
					frequency_sum += delta
				else:
					frequency_sum -= delta
				
				line = fp.readline().strip()
				
				if frequency_sum in known_frequencies and not found_repeat:
					first_repeat = frequency_sum
					found_repeat = True
					break
				known_frequencies.append(frequency_sum)
				
		if first_pass:
			print("Calibration: %s" % frequency_sum)
			first_pass = False
	
	print("First repeat frequency: %s" % first_repeat)
	

if __name__ == "__main__":
	main()

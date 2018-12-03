#!/usr/bin/env python

def main():
	
	with open("input.txt") as input_file:
		lines = input_file.read().strip().split()
	
	double_count = 0
	triple_count = 0
	for block in lines:
		if check_for_count(block, 3):
			triple_count += 1
		if check_for_count(block, 2):
			double_count += 1
	
	print("Checksum: %d" % (triple_count * double_count))
	print("Shared letters: %s" % find_match(lines))

def check_for_count(string, num):
	unique_letters = []
	for l in string:
		if not l in unique_letters:
			unique_letters.append(l)
	for u in unique_letters:
		count = string.count(u)
		if count == num:
			return True
	return False

def find_match(lines):
	for block_a in lines:
		for block_b in lines:
			shared = check_match(block_a, block_b)
			if not shared == "":
				return shared

def check_match(string_a, string_b):
	mismatch_count = 0
	for i in range(0, len(string_a)):
		if not string_a[i:i+1] == string_b[i:i+1]:
			mismatch_count += 1
	shared = ""
	if mismatch_count == 1:
		for a in string_a:
			if a in string_b:
				shared += a
	return shared

if __name__ == "__main__":
	main()

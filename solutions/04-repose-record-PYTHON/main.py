#!/usr/bin/env python3

from collections import defaultdict

def main():
	
	with open("input.txt") as input_file:
		lines = input_file.read().strip().split("\n")
	
	lines.sort()
	
	guard_map = defaultdict(lambda: {minute: 0 for minute in range(0, 60)})
	
	current_guard = 0
	for i in range(0, len(lines)):
		current_line = lines[i]
		if "begins shift" in current_line:
			current_guard = get_guard(current_line)
		elif "wakes up" in current_line:
			continue
		else:
			next_line = lines[i + 1]
			current_minute = get_minute(current_line)
			next_minute = get_minute(next_line)
			for m in range(current_minute, next_minute):
				guard_map[current_guard][m] += 1
	
	sleep_times = defaultdict(int)
	sleepiest_guard = 0
	for guard in list(guard_map):
		if sum(guard_map[guard].values()) > sum(guard_map[sleepiest_guard].values()):
			sleepiest_guard = guard
	
	print("Sleepiest guard: %d" % sleepiest_guard)
	
	most_slept_minute = get_most_slept_minute(guard_map[sleepiest_guard])
	
	print("Most slept minute: %d" % most_slept_minute)
	print("Part 1 answer: %d" % (sleepiest_guard * most_slept_minute))
	
	most_consistent_guard = 0
	for guard in list(guard_map):
		if max(guard_map[guard].values()) > max(guard_map[most_consistent_guard].values()):
			most_consistent_guard = guard
	
	print("Most consistent guard: %d" % most_consistent_guard)
	most_consistent_minute = get_most_slept_minute(guard_map[most_consistent_guard])
	print("Most consistent minute: %d" % most_consistent_minute)
	print("Part 2 answer: %d" % (most_consistent_guard * most_consistent_minute))
	

def get_minute(string):
	return int(string.split()[1].replace("]", "").split(":")[1])

def get_guard(string):
	return int(string.split()[3].replace("#", ""))

def get_most_slept_minute(minutes):
	return max(minutes, key=minutes.get)

if __name__ == "__main__":
	main()


lines = File.read_lines("input.txt", chomp: true).sort

guard_map = Hash(UInt32, Array(UInt32)).new

current_guard = 0
(0...lines.size).each do |i|
	current_line = lines[i]
	if current_line.includes? "begins shift"
		current_guard = get_guard(current_line)
		guard_map[current_guard] = Array(UInt32).new(60, 0) unless guard_map[current_guard]?
	elsif current_line.includes? "wakes up"
		next
	else
		current_minute = get_minute(current_line)
		next_minute = get_minute(lines[i + 1])
		(current_minute...next_minute).each do |m|
			guard_map[current_guard][m] += 1
		end
	end
end

sleepiest_guard = 0
most_consistent_guard = 0
guard_map.each do |guard, minutes|
	sleepiest_guard = guard if sleepiest_guard == 0 || minutes.sum > guard_map[sleepiest_guard].sum
	most_consistent_guard = guard if most_consistent_guard == 0 || minutes.max > guard_map[most_consistent_guard].max
end
most_slept_minute = guard_map[sleepiest_guard].each_with_index.max[1]
most_consistent_minute = guard_map[most_consistent_guard].each_with_index.max[1]

puts "Part 1 answer: #{sleepiest_guard * most_slept_minute}"
puts "Part 2 answer: #{most_consistent_guard * most_consistent_minute}"

def get_minute(line)
	line.split[1].tr("]", "").split(":")[1].to_u32
end

def get_guard(line)
	line.split[3].tr("#", "").to_u32
end

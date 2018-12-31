
double_count = 0
triple_count = 0

lines = File.read_lines("input.txt", chomp: true)

def check_for_count(string, num)
	string.chars.uniq.each do |c|
		if string.count(c) == num
			return true
		end
	end
	return false
end

lines.each do |line|
	double_count += 1 if check_for_count(line, 2)
	triple_count += 1 if check_for_count(line, 3)
end

puts "Checksum: #{double_count * triple_count}"

lines.each do |block_a|
	lines.each do |block_b|
		mismatches = 0
		shared = ""
		block_a.chars.zip(block_b.chars) do |a, b|
			if a != b
				mismatches += 1
			else
				shared += a
			end
		end
		if mismatches == 1
			puts "Shared letters: #{shared}"
			exit 0
		end
	end
end

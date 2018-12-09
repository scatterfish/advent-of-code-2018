
frequency_deltas = [] of Int32
frequency_sum = 0
known_frequencies = Set(Int32).new
first_repeat = 0

File.each_line("input.txt", chomp: true) do |line|
	delta = line.to_i
	frequency_deltas << delta
end

found_repeat = false
first_loop = true
while !found_repeat
	frequency_deltas.each do |delta|
		frequency_sum += delta
		if known_frequencies.includes? frequency_sum
			first_repeat = frequency_sum
			found_repeat = true
			break
		end
		known_frequencies << frequency_sum
	end
	if first_loop
		puts "Calibration: #{frequency_sum}"
		first_loop = false
	end
end

puts "First repeat frequency: #{first_repeat}"

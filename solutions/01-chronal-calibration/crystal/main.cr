
frequency_deltas = File.read_lines("input.txt", chomp: true).map(&.to_i)

puts "Calibration frequency: #{frequency_deltas.sum}"

frequency_sum = 0
known_frequencies = Set(Int32).new
frequency_deltas.cycle do |delta|
	frequency_sum += delta
	if known_frequencies.includes? frequency_sum
		puts "First repeat frequency: #{frequency_sum}"
		break
	end
	known_frequencies << frequency_sum
end

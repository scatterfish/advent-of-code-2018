
SEARCH_SIZE = 300 # how many sizes to brute force, answers always seem to be < 20

serial_num = File.read("input.txt").strip.to_u32

grid = Array.new(300) { Array.new(300, 0) }

(0...300).each do |x|
	(0...300).each do |y|
		grid[x][y] = get_power_level(x, y, serial_num)
	end
end

results = Array(Array(Int32)).new(SEARCH_SIZE)

(1..SEARCH_SIZE).each do |size|
	puts "Size #{size} starting..."
	max_power = 0
	x_coord = 0
	y_coord = 0
	(0..300 - size).each do |x|
		(0..300 - size).each do |y|
			power_level = 0
			(0...size).each do |box_x|
				(0...size).each do |box_y|
					power_level += grid[x + box_x][y + box_y]
				end
			end
			if power_level > max_power
				max_power = power_level
				x_coord = x + 1
				y_coord = y + 1
			end
		end
	end
	puts "Size #{size} done"
	results << [x_coord, y_coord, max_power]
end

x_2 = 0
y_2 = 0
size = 0
max_power = 0
(1..SEARCH_SIZE).each do |s|
	x, y, p = results[s - 1]
	if s == 3
		puts "Part 1 answer: #{x},#{y}"
	end
	if p > max_power
		max_power = p
		x_2 = x
		y_2 = y
		size = s
	end
end
puts "Part 2 answer: #{x_2},#{y_2},#{size}"

def get_power_level(x, y, serial)
	rack_id = (x + 1) + 10
	power_level = rack_id * (y + 1)
	power_level += serial
	power_level *= rack_id
	power_level = ((power_level / 100) % 10).floor
	power_level -= 5
	power_level
end

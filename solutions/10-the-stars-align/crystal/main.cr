
struct Particle
	property x_pos : Int32
	property y_pos : Int32
	property x_vel : Int32
	property y_vel : Int32
	def initialize(@x_pos, @y_pos, @x_vel, @y_vel)
	end
end

particles = Set(Particle).new

File.read_lines("input.txt", chomp: true).each do |line|
	x_pos = line[10...16].to_i
	y_pos = line[17...24].to_i
	x_vel = line[36...38].to_i
	y_vel = line[39...42].to_i
	particles << Particle.new(x_pos, y_pos, x_vel, y_vel)
end

min_size = 1000000
time = 0
1.step do |i|
	x_min, x_max = particles.map { |p| p.x_pos + (p.x_vel * i) }.minmax
	y_min, y_max = particles.map { |p| p.y_pos + (p.y_vel * i) }.minmax
	size = (x_max - x_min) + (y_max - y_min)
	if size < min_size
		min_size = size
		time = i
	else
		break
	end
end

x_pos_list = particles.map { |p| p.x_pos + (p.x_vel * time) }
y_pos_list = particles.map { |p| p.y_pos + (p.y_vel * time) }
x_min, x_max = x_pos_list.minmax
y_min, y_max = y_pos_list.minmax

grid = Array.new(y_max - y_min + 1) { Array.new(x_max - x_min + 1, ' ') }

x_pos_list.zip(y_pos_list).each do |x, y|
	grid[y - y_min][x - x_min] = '█'
end

grid.each do |row|
	puts row.join("")
end

puts "Answer found at time #{time}"

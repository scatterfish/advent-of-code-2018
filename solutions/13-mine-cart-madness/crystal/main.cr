
class Cart
	property x         : Int32
	property y         : Int32
	property name      : Char
	property direction : Symbol
	property last_turn : Symbol
	def initialize(@name, @x, @y, @direction)
		@last_turn = :right
	end
end

LEFT_MAP = {
	:up => :left,
	:right => :up,
	:down => :right,
	:left => :down,
}

RIGHT_MAP = {
	:up => :right,
	:right => :down,
	:down => :left,
	:left => :up,
}

grid = File.read_lines("input.txt", chomp: true).map(&.chars)

carts = Array(Cart).new

names = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".chars.reverse
grid.size.times do |y|
	grid[y].size.times do |x|
		case grid[y][x]
		when '^'
			carts << Cart.new(names.pop, x, y, :up)
		when '>'
			carts << Cart.new(names.pop, x, y, :right)
		when 'v'
			carts << Cart.new(names.pop, x, y, :down)
		when '<'
			carts << Cart.new(names.pop, x, y, :left)
		end
	end
end

first_crash = {-1, -1}

time = 0
crashed = Set(Cart).new
while carts.size > 1
	carts.sort! { |a, b| a.x + (a.y * 999) <=> b.x + (b.y * 999) }
	crashed.clear
	carts.each do |cart|
		case cart.direction
		when :up
			cart.y -= 1
			case grid[cart.y][cart.x]
			when '/'
				cart.direction = :right
			when '\\'
				cart.direction = :left
			end
		when :right
			cart.x += 1
			case grid[cart.y][cart.x]
			when '/'
				cart.direction = :up
			when '\\'
				cart.direction = :down
			end
		when :down
			cart.y += 1
			case grid[cart.y][cart.x]
			when '/'
				cart.direction = :left
			when '\\'
				cart.direction = :right
			end
		when :left
			cart.x -= 1
			case grid[cart.y][cart.x]
			when '/'
				cart.direction = :down
			when '\\'
				cart.direction = :up
			end
		end
		if grid[cart.y][cart.x] == '+'
			cycle_direction(cart)
		end
		carts.each do |other|
			if cart != other && cart.x == other.x && cart.y == other.y
				puts "Crash between #{cart.name} and #{other.name} at #{cart.x},#{cart.y} at time #{time}"
				if first_crash == {-1, -1}
					first_crash = {cart.x, cart.y}
				end
				crashed << cart
				crashed << other
			end
		end
	end
	crashed.each do |cart|
		carts.delete(cart)
	end
	time += 1
end

puts "───────────────────────────────────────────────"
puts "First crash location: #{first_crash[0]},#{first_crash[1]}"
puts "Last remaining cart location: #{carts[0].x},#{carts[0].y}"

def cycle_direction(cart)
	case cart.last_turn
	when :left
		cart.last_turn = :straight
	when :straight
		cart.direction = RIGHT_MAP[cart.direction]
		cart.last_turn = :right
	when :right
		cart.direction = LEFT_MAP[cart.direction]
		cart.last_turn = :left
	end
end

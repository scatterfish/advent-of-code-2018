
class Cart
	property x         : Int32
	property y         : Int32
	property direction : Symbol
	property last_turn : Symbol
	def initialize(@x, @y, @direction)
		@last_turn = :right
	end
end

LEFT_MAP = {
	:up    => :left,
	:right => :up,
	:down  => :right,
	:left  => :down,
}

RIGHT_MAP = {
	:up    => :right,
	:right => :down,
	:down  => :left,
	:left  => :up,
}

grid = File.read_lines("input.txt", chomp: true).map(&.chars)

carts = Array(Cart).new

grid.size.times do |y|
	grid[y].size.times do |x|
		case grid[y][x]
		when '^'
			carts << Cart.new(x, y, :up)
		when '>'
			carts << Cart.new(x, y, :right)
		when 'v'
			carts << Cart.new(x, y, :down)
		when '<'
			carts << Cart.new(x, y, :left)
		end
	end
end

first_crash = {-1, -1}

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
		cycle_direction(cart) if grid[cart.y][cart.x] == '+'
		carts.each do |other|
			if cart != other && cart.x == other.x && cart.y == other.y
				first_crash = {cart.x, cart.y} if first_crash == {-1, -1}
				crashed << cart
				crashed << other
			end
		end
	end
	crashed.each do |cart|
		carts.delete(cart)
	end
end

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

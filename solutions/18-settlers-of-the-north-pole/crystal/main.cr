
SEARCH_WAIT = 700 # how many iterations to wait before looking for a loop

grid = File.read_lines("input.txt", chomp: true).map(&.chars)

resource_snapshots = Array(Int32).new

grid_next = Array(Char).new
adjacent_tiles = Array(Char).new
1.step do |i|
	grid_next = grid.clone
	grid.size.times do |x|
		grid[x].size.times do |y|
			adjacent_tiles.clear
			((x > 0 ? -1 : 0)..(x < grid.size - 1 ? 1 : 0)).each do |adj_x|
				((y > 0 ? -1 : 0)..(y < grid[x].size - 1 ? 1 : 0)).each do |adj_y|
					adjacent_tiles << grid[x + adj_x][y + adj_y] if adj_x != 0 || adj_y != 0
				end
			end
			case grid[x][y]
			when '.'
				grid_next[x][y] = '|' if adjacent_tiles.count('|') >= 3
			when '|'
				grid_next[x][y] = '#' if adjacent_tiles.count('#') >= 3
			when '#'
				grid_next[x][y] = '.' if adjacent_tiles.count('#') < 1 || adjacent_tiles.count('|') < 1
			end
		end
	end
	grid = grid_next
	value = get_resource_value(grid)
	puts "Part 1 answer: #{value}" if i == 10
	if i > SEARCH_WAIT
		if resource_snapshots.includes? value
			answer_index = (1000000000 - i) % resource_snapshots.size
			puts "Part 2 answer: #{resource_snapshots[answer_index]}"
			break
		else
			resource_snapshots << value
		end
	end
end

def get_resource_value(grid)
	tree_count = 0
	lumberyard_count = 0
	grid.each do |row|
		tree_count += row.count('|')
		lumberyard_count += row.count('#')
	end
	tree_count * lumberyard_count
end

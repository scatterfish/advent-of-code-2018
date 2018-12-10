
chain = File.read("input.txt").strip

puts "Reacting polymer chain..."
chain = react_polymer_chain(chain)
puts "Units left after reaction: #{chain.size}"

puts "Testing polymer shrinks..."
puts "Minimum polymer length: #{get_min_length(chain)}"

def react_polymer_chain(chain)
	i = 0
	while i < chain.size - 1
		if chain[i] != chain[i + 1] && chain[i].downcase == chain[i + 1].downcase
			chain = chain[0...i] + chain[i + 2..-1]
			i = [0, i - 1].max
		else
			i += 1
		end
	end
	chain
end

def get_min_length(chain)
	min_length = chain.size
	"abcdefghijklmnopqrstuvwxyz".each_char do |u|
		chain_shrink = chain.delete(u).delete(u.upcase)
		shrink_length = react_polymer_chain(chain_shrink).size
		min_length = [min_length, shrink_length].min
	end
	min_length
end

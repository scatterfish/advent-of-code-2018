
recipe_count = File.read("input.txt").strip().to_u32

recipes = [3, 7]

elf_a_i = 0
elf_b_i = 1

seq_target = recipe_count.to_s.chars
seq_i = 0

1.step do |i|
	recipe_a = recipes[elf_a_i]
	recipe_b = recipes[elf_b_i]
	(recipe_a + recipe_b).to_s.each_char do |r|
		recipes << r.to_i
		if r == seq_target[seq_i]
			seq_i += 1
			if seq_i == seq_target.size
				puts "Part 2 answer: #{recipes.size - seq_target.size}"
				exit 0
			end
		else
			seq_i = 0
		end
	end
	puts "Part 1 answer: #{recipes[recipe_count...recipe_count + 10].join("")}" if i == recipe_count + 10
	elf_a_i = (elf_a_i + recipe_a + 1) % recipes.size
	elf_b_i = (elf_b_i + recipe_b + 1) % recipes.size
end

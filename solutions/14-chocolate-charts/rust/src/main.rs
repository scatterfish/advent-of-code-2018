
use std::process;

fn main() {
	
	let input = include_str!("input.txt").trim();
	
	let recipe_count = input.parse::<usize>().unwrap();
	let seq_target: Vec<usize> = get_digits(recipe_count);
	
	let mut recipes = vec![3, 7];
	
	let mut elf_a_i = 0;
	let mut elf_b_i = 1;
	
	let mut seq_i = 0;
	
	let mut i = 0;
	loop {
		let recipe_a = recipes[elf_a_i];
		let recipe_b = recipes[elf_b_i];
		for r in get_digits(recipe_a + recipe_b) {
			recipes.push(r);
			if r == seq_target[seq_i] {
				seq_i += 1;
				if seq_i == seq_target.len() {
					println!("Part 2 answer: {}", recipes.len() - seq_target.len());
					process::exit(0);
				}
			} else {
				seq_i = 0;
			}
		}
		if i == recipe_count + 10 {
			// yikes
			println!("Part 1 answer: {}", recipes.get(recipe_count..recipe_count + 10).unwrap().iter().map(|n| n.to_string()).collect::<String>());
		}
		elf_a_i = (elf_a_i + recipe_a + 1) % recipes.len();
		elf_b_i = (elf_b_i + recipe_b + 1) % recipes.len();
		i += 1;
	}
	
}

fn get_digits(n: usize) -> Vec<usize> {
	// getting the digits this way is slightly faster than doing int -> string, string -> vec<char>, vec<char> -> vec<int>
	let mut digits = Vec::new();
	let mut n = n;
	while n > 9 {
		digits.push(n % 10);
		n /= 10;
	}
	digits.push(n);
	digits.reverse();
	digits
}

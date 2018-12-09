
// yeah, I think I'm done with Rust for general-purpose stuff (especially involving strings)

use std::process;

fn main() {
	
	let mut chain = include_str!("input.txt").trim().to_string();
	
	println!("Reacting polymer chain...");
	chain = react_polymer_chain(chain);
	println!("Units left after reaction: {}", chain.len());
	
	println!("Testing polymer shrinks...");
	println!("Minimum polymer length: {}", get_min_length(chain));
	
}

fn react_polymer_chain(chain: String) -> String {
	let mut chain = chain;
	let mut i = 0;
	while i < chain.len() - 1 {
		let current_char = get_char_at(&chain, i);
		let next_char = get_char_at(&chain, i + 1);
		if current_char != next_char && current_char.to_ascii_lowercase() == next_char.to_ascii_lowercase() {
			let chain_back = get_mut_string_section(&chain, i + 2, chain.len());
			chain = get_mut_string_section(&chain, 0, i);
			chain.push_str(chain_back.as_str());
			if i != 0 { i -= 1; }
		} else {
			i += 1;
		}
	}
	chain.to_string()
}

fn get_min_length(chain: String) -> usize {
	let mut min_length = chain.len();
	for u in "abcdefghijklmnopqrstuvwxyz".chars() {
		let chain_shrink = chain.replace(u, "").replace(u.to_ascii_uppercase(), "");
		let shrink_len = react_polymer_chain(chain_shrink).len();
		if shrink_len < min_length { min_length = shrink_len; }
	}
	min_length
}

fn get_char_at(string: &str, i: usize) -> char {
	match string.chars().nth(i) {
		Some(c) => c,
		None => {
			eprintln!("Tried to get char from \"{}\" at index {} but got nothing!", string, i);
			process::exit(1);
		}
	}
}

fn get_mut_string_section(string: &str, start: usize, end: usize) -> String {
	match string.get(start..end) {
		Some(s) => s,
		None => {
			eprintln!("Tried to get slice of \"{}\" from \"{}\" to \"{}\" but got nothing!", string, start, end);
			process::exit(1);
		}
	}.to_string()
}

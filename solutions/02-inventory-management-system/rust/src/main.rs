
use std::collections::HashSet;
use std::iter::FromIterator;

fn main() {
	
	let input = include_str!("input.txt");
	let input_lines: Vec<&str> = input.lines().collect();
	
	let mut double_count = 0;
	let mut triple_count = 0;
	for line in &input_lines {
		if check_for_count(&line, 3) { triple_count += 1; }
		if check_for_count(&line, 2) { double_count += 1; }
	}
	
	println!("Checksum: {}", triple_count * double_count);
	println!("Shared letters: {}", find_match(input_lines));
	
}

fn check_for_count(string: &str, num: usize) -> bool {
	
	let unique_letters: HashSet<char> = HashSet::from_iter(string.chars());
	
	for u in unique_letters {
		let count = string.matches(u).count();
		if count == num {
			return true;
		}
	}
	return false;
	
}

fn find_match(lines: Vec<&str>) -> String {
	
	for line_a in &lines {
		for line_b in &lines {
			let shared = check_match(line_a, line_b);
			if shared != "" {
				return shared;
			}
		}
	}
	return String::from("");
	
}

fn check_match(string_a: &str, string_b: &str) -> String {
	
	let mut mismatch_count = 0;
	
	for i in 0..string_a.len() {
		if &string_a[i..i+1] != &string_b[i..i+1] {
			mismatch_count += 1;
		}
	}
	let mut shared_chars = String::new();
	if mismatch_count == 1 {
		for a in string_a.chars() {
			if string_b.contains(a) {
				shared_chars.push(a);
			}
		}
	}
	return shared_chars;
	
}

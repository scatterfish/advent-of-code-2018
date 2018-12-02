
use std::process;
use std::collections::HashSet;

fn main() {
	
	let input = include_str!("input.txt");
	
	let input_lines: Vec<&str> = input.lines().collect();
	let mut frequency_deltas: Vec<i32> = Vec::new();
	
	for line in input_lines {
		let delta = match line.parse::<i32>() {
			Ok(i) => i,
			Err(e) => {
				eprintln!("Error while trying to parse input deltas!\n{}", e);
				process::exit(1)
			}
		};
		frequency_deltas.push(delta);
	}
	
	let mut frequency_sum = 0;
	let mut first_repeat = 0;
	let mut known_frequencies: HashSet<i32> = HashSet::new();
	
	let mut found_repeat = false;
	let mut first_loop = true;
	while !found_repeat {
		for i in &frequency_deltas {
			frequency_sum += i;
			if known_frequencies.contains(&frequency_sum) {
				first_repeat = frequency_sum;
				found_repeat = true;
				break;
			}
			known_frequencies.insert(frequency_sum);
		}
		if first_loop {
			println!("Calibration: {}", frequency_sum);
			first_loop = false;
		}
	}
	println!("First repeat frequency: {}", first_repeat);
	
}

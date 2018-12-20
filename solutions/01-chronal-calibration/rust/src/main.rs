
use std::collections::HashSet;

fn main() {
	
	let input = include_str!("input.txt");
	
	let frequency_deltas: Vec<i32> = input.lines().map(|n| n.parse::<i32>().unwrap()).collect();
	
	println!("Calibration frequency: {}", frequency_deltas.iter().sum::<i32>());
	
	let mut frequency_sum = 0;
	let mut known_frequencies: HashSet<i32> = HashSet::new();
	for delta in frequency_deltas.iter().cycle() {
		frequency_sum += delta;
		if known_frequencies.contains(&frequency_sum) {
			println!("First repeat frequency: {}", frequency_sum);
			break;
		}
		known_frequencies.insert(frequency_sum);
	}
	
}

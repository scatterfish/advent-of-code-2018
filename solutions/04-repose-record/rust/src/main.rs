
use std::process;
use std::collections::HashMap;

fn main() {
	
	let input = include_str!("input.txt");
	let mut input_lines: Vec<&str> = input.lines().collect();
	
	input_lines.sort_unstable();
	
	let mut guard_map: HashMap<usize, [usize; 60]> = HashMap::new();
	
	let mut current_guard = 0;
	for i in 0..input_lines.len() {
		let current_line = input_lines[i];
		if current_line.contains("begins shift") {
			current_guard = get_gaurd(current_line);
		} else if current_line.contains("wakes up") {
			continue;
		} else {
			let next_line = input_lines[i + 1];
			let current_minute = get_minute(current_line);
			let next_minute = get_minute(next_line);
			for m in current_minute..next_minute {
				guard_map.entry(current_guard).or_insert([0; 60])[m] += 1;
			}
		}
	}
	
	let mut sleepiest_guard = 0;
	let mut most_consistent_guard = 0;
	for guard in guard_map.keys() {
		if sleepiest_guard == 0 || sum_int_arr(guard_map[guard]) > sum_int_arr(guard_map[&sleepiest_guard]) {
			sleepiest_guard = *guard;
		}
		if most_consistent_guard == 0 || get_max_slept(guard_map[guard]) > get_max_slept(guard_map[&most_consistent_guard]) {
			most_consistent_guard = *guard;
		}
	}
	let most_slept_minute = get_most_slept_minute(guard_map[&sleepiest_guard]);
	let most_consistent_minute = get_most_slept_minute(guard_map[&most_consistent_guard]);
	
	println!("Part 1 answer: {}", sleepiest_guard * most_slept_minute);
	println!("Part 2 answer: {}", most_consistent_guard * most_consistent_minute);
	
}

fn parse_int(s: &str) -> usize {
	match s.trim().parse::<usize>() {
		Ok(i) => i,
		Err(e) => {
			eprintln!("Error while trying to parse \"{}\" as int!\n{}", s, e);
			process::exit(1);
		}
	}
}

fn sum_int_arr(arr: [usize; 60]) -> usize {
	arr.iter().fold(0, |a, &b| a + b)
}

fn get_minute(string: &str) -> usize {
	let mut minute_str = string.split(' ').collect::<Vec<&str>>()[1];
	minute_str = &minute_str[0..minute_str.len() - 1];
	minute_str = minute_str.split(':').collect::<Vec<&str>>()[1];
	parse_int(minute_str)
}

fn get_gaurd(string: &str) -> usize {
	let mut guard_str: &str = string.split(' ').collect::<Vec<&str>>()[3];
	guard_str = &guard_str[1..guard_str.len()];
	parse_int(guard_str)
}

fn get_most_slept_minute(minutes: [usize; 60]) -> usize {
	let mut best_minute = 0;
	for i in 0..60 {
		if minutes[i] > minutes[best_minute] {
			best_minute = i;
		}
	}
	best_minute
}

fn get_max_slept(minutes: [usize; 60]) -> usize {
	let mut max_slept = 0;
	for i in 0..60 {
		if minutes[i] > max_slept {
			max_slept = minutes[i];
		}
	}
	max_slept
}

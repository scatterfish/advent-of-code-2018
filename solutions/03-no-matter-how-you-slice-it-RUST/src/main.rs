
use std::process;

struct Claim {
	id: usize,
	width_lower: usize,
	width_upper: usize,
	height_lower: usize,
	height_upper: usize,
}

fn main() {
	
	let input = include_str!("input.txt");
	let input_lines: Vec<&str> = input.lines().collect();
	
	let mut grid = [[0; 1000]; 1000];
	
	let mut claim_list: Vec<Claim> = Vec::new();
	
	for l in &input_lines {
		let id          = parse_int(&l[find_char(l, '#') + 1..find_char(l, '@')]);
		let margin_left = parse_int(&l[find_char(l, '@') + 1..find_char(l, ',')]);
		let margin_top  = parse_int(&l[find_char(l, ',') + 1..find_char(l, ':')]);
		let width       = parse_int(&l[find_char(l, ':') + 1..find_char(l, 'x')]);
		let height      = parse_int(&l[find_char(l, 'x') + 1..]);
		claim_list.push(Claim {
			id: id,
			width_lower: margin_left,
			width_upper: margin_left + width,
			height_lower: margin_top,
			height_upper: margin_top + height,
		});
	}
	
	for claim in &claim_list {
		for x in claim.width_lower..claim.width_upper {
			for y in claim.height_lower..claim.height_upper {
				grid[x][y] += 1;
			}
		}
	}
	
	let mut overlap_count = 0;
	for x in 0..1000 {
		for y in 0..1000 {
			if grid[x][y] > 1 { overlap_count += 1; }
		}
	}
	println!("Overlapping tiles: {}", overlap_count);
	
	for claim in claim_list {
		let mut is_valid = true;
		for x in claim.width_lower..claim.width_upper {
			for y in claim.height_lower..claim.height_upper {
				if grid[x][y] > 1 { is_valid = false; }
			}
		}
		if is_valid {
			println!("Valid claim: {}", claim.id);
			break;
		}
	}
	
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

fn find_char(s: &str, t: char) -> usize {
	match s.chars().position(|c| c == t) {
		Some(n) => n,
		None => {
			eprintln!("Error while trying to find index of \'{}\' in \"{}\"!", t, s);
			process::exit(1);
		}
	}
}

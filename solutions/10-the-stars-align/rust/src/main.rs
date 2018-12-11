
use std::process;

struct Particle {
	x_pos: isize,
	y_pos: isize,
	x_vel: isize,
	y_vel: isize,
}

fn main() {
	
	let input = include_str!("input.txt");
	let input_lines: Vec<&str> = input.lines().collect();
	
	let mut particles: Vec<Particle> = Vec::new();
	
	for line in &input_lines {
		let x_pos = parse_int(&line[10..16]);
		let y_pos = parse_int(&line[17..24]);
		let x_vel = parse_int(&line[36..38]);
		let y_vel = parse_int(&line[39..42]);
		particles.push(Particle {
			x_pos: x_pos,
			y_pos: y_pos,
			x_vel: x_vel,
			y_vel: y_vel,
		});
	}
	
	let mut min_size = 1000000;
	let mut time = 0;
	for i in 0..1000000 {
		let x_pos_list: Vec<isize> = particles.iter().map(|p| p.x_pos + (p.x_vel * i)).collect();
		let y_pos_list: Vec<isize> = particles.iter().map(|p| p.y_pos + (p.y_vel * i)).collect();
		let (x_min, x_max) = minmax(&x_pos_list);
		let (y_min, y_max) = minmax(&y_pos_list);
		let size = (x_max - x_min) + (y_max - y_min);
		if size < min_size {
			min_size = size;
			time = i;
		} else {
			break;
		}
	}
	
	let x_pos_list: Vec<isize> = particles.iter().map(|p| p.x_pos + (p.x_vel * time)).collect();
	let y_pos_list: Vec<isize> = particles.iter().map(|p| p.y_pos + (p.y_vel * time)).collect();
	let (x_min, x_max) = minmax(&x_pos_list);
	let (y_min, y_max) = minmax(&y_pos_list);
	
	let mut grid = vec![vec![' '; (x_max - x_min + 1) as usize]; (y_max - y_min + 1) as usize];
	
	for (x, y) in x_pos_list.iter().zip(y_pos_list.iter()) {
		grid[(y - y_min) as usize][(x - x_min) as usize] = '█';
	}
	
	for row in grid {
		println!("{}", row.iter().collect::<String>());
	}
	
	println!("Answer found at time {}", time);
	
}

fn parse_int(s: &str) -> isize {
	match s.trim().parse::<isize>() {
		Ok(i) => i,
		Err(e) => {
			eprintln!("Error while trying to parse \"{}\" as int!\n{}", s, e);
			process::exit(1);
		}
	}
}

fn minmax(v: &Vec<isize>) -> (isize, isize) {
	let min = match v.iter().min() {
		Some(n) => n,
		None => {
			eprintln!("Tried to find min of \"{:?}\" but found none!", v);
			process::exit(1);
		}
	};
	let max = match v.iter().max() {
		Some(n) => n,
		None => {
			eprintln!("Tried to find max of \"{:?}\" but found none!", v);
			process::exit(1);
		}
	};
	(*min, *max)
}

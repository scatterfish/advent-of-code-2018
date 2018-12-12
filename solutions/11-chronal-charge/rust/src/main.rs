extern crate threadpool;

use std::process;
use std::sync::mpsc::channel;
use threadpool::ThreadPool;

const THREAD_COUNT: usize = 8;

fn main() {
	
	let serial_num = parse_int(include_str!("input.txt"));
	
	let mut grid: [[isize; 300]; 300] = [[0; 300]; 300];
	
	for x in 0..300 {
		for y in 0..300 {
			grid[x][y] = get_power_level(x, y, serial_num);
		}
	}
	
	let pool = ThreadPool::new(THREAD_COUNT);
	
	let (tx, rx) = channel();
	for size in 0..300 {
		let tx = tx.clone();
		pool.execute(move || {
			tx.send(calculate_power_data(size + 1, grid)).unwrap();
		});
	}
	
	let mut x_1 = 0;
	let mut y_1 = 0;
	let mut x_2 = 0;
	let mut y_2 = 0;
	let mut size = 0;
	let mut max_power = 0;
	for _ in 0..300 {
		let (x, y, s, p) = rx.recv().unwrap();
		if s == 3 {
			x_1 = x;
			y_1 = y;
		}
		if p > max_power {
			max_power = p;
			x_2 = x;
			y_2 = y;
			size = s;
		}
	}
	
	println!("Part 1 answer: {},{}", x_1, y_1);
	println!("Part 2 answer: {},{},{}", x_2, y_2, size);
	
}

fn calculate_power_data(size: usize, grid: [[isize; 300]; 300]) -> (isize, isize, isize, isize) {
	println!("Size {} starting...", size);
	let mut max_power = 0;
	let mut x_coord = 0;
	let mut y_coord = 0;
	for x in 0..300 - size + 1 {
		for y in 0..300 - size + 1 {
			let mut power_level = 0;
			for box_x in 0..size {
				for box_y in 0..size {
					power_level += grid[x + box_x][y + box_y];
				}
			}
			if power_level > max_power {
				max_power = power_level;
				x_coord = (x + 1) as isize;
				y_coord = (y + 1) as isize;
			}
		}
	}
	println!("Size {} done", size);
	(x_coord, y_coord, size as isize, max_power)
}

fn get_power_level(x: usize, y: usize, serial: usize) -> isize {
	// welcome to casting hell
	let rack_id = (x + 1) + 10;
	let mut power_level: isize = (rack_id * (y + 1)) as isize;
	power_level += serial as isize;
	power_level *= rack_id as isize;
	power_level = ((power_level / 100) % 10) as isize;
	power_level -= 5;
	power_level
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

#!/usr/bin/env python3

import networkx as nx

def main():
	
	with open("input.txt") as input_file:
		lines = input_file.read().strip().split("\n")
	
	steps_graph = nx.DiGraph()
	
	for l in lines:
		pieces = l.split()
		req = pieces[1]
		step = pieces[7]
		steps_graph.add_edge(req, step)
	
	steps_sorted = nx.lexicographical_topological_sort(steps_graph)
	steps = "".join(steps_sorted)
	
	print("Steps order: %s" % steps)
	
	time = 0
	tasks = []
	time_map = {task: time + 60 for task, time in zip(sorted(steps), range(1, len(steps) + 1))}
	
	while steps_graph or tasks:
		available_steps = [s for s in steps_graph if s not in [t[0] for t in tasks] and steps_graph.in_degree(s) == 0]
		if available_steps and len(tasks) < 5:
			task = min(available_steps)
			tasks.append((task, time_map[task]))
		else:
			next_time = min([t[1] for t in tasks])
			time += next_time
			tasks = [(task, time - next_time) for task, time in tasks]
			finished_tasks = [t for t in tasks if t[1] == 0]
			for task in finished_tasks:
				tasks.remove(task)
			steps_graph.remove_nodes_from([t[0] for t in finished_tasks])
	
	print("Time taken: %d" % time)
	

if __name__ == "__main__":
	main()

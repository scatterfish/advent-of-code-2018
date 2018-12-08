#!/usr/bin/env python3

class Node:
	def __init__(self):
		self.children_count = 0
		self.metadata_count = 0
		self.child_nodes = []
		self.metadata = []

node_data = []

def main():
	global node_data
	
	with open("input.txt") as input_file:
		node_data = [int(n) for n in reversed(input_file.read().strip().split())]
	
	root = get_tree_from_data()
	
	print("Metadata sum: %d" % get_metadata_sum(root))
	
	print("Root value: %d" % get_node_value(root))
	

def get_tree_from_data():
	node = Node()
	node.children_count = pop_data()
	node.metadata_count = pop_data()
	if node.children_count != 0:
		child_index = 0
		while child_index < node.children_count:
			node.child_nodes.append(get_tree_from_data())
			child_index += 1
	metadata_index = 0
	while metadata_index < node.metadata_count:
		node.metadata.append(pop_data())
		metadata_index += 1
	return node

def get_metadata_sum(node):
	metadata_sum = sum(node.metadata)
	if node.children_count == 0:
		return metadata_sum
	else:
		return metadata_sum + sum([get_metadata_sum(n) for n in node.child_nodes])

def get_node_value(node):
	metadata_sum = sum(node.metadata)
	if node.children_count == 0:
		return metadata_sum
	else:
		value = 0
		for index in [i for i in node.metadata if i <= node.children_count]:
			value += get_node_value(node.child_nodes[index - 1])
		return value

def pop_data():
	return node_data.pop()

if __name__ == "__main__":
	main()

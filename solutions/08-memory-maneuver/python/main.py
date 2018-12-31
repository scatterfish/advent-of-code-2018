#!/usr/bin/env python3

class Node:
	def __init__(self):
		self.children_count = 0
		self.metadata_count = 0
		self.child_nodes = []
		self.metadata = []

def main():
	
	with open("input.txt") as input_file:
		node_data = [int(n) for n in reversed(input_file.read().strip().split())]
	
	root = get_tree_from_data(node_data)
	
	print("Metadata sum: %d" % get_metadata_sum(root))
	print("Root value: %d" % get_node_value(root))
	

def get_tree_from_data(data):
	node = Node()
	node.children_count = data.pop()
	node.metadata_count = data.pop()
	for _ in range(node.children_count):
		node.child_nodes.append(get_tree_from_data(data))
	for _ in range(node.metadata_count):
		node.metadata.append(data.pop())
	return node

def get_metadata_sum(node):
	metadata_sum = sum(node.metadata)
	if node.children_count == 0:
		return metadata_sum
	else:
		return metadata_sum + sum([get_metadata_sum(n) for n in node.child_nodes])

def get_node_value(node):
	if node.children_count == 0:
		return sum(node.metadata)
	else:
		value = 0
		for index in [i for i in node.metadata if i <= node.children_count]:
			value += get_node_value(node.child_nodes[index - 1])
		return value

if __name__ == "__main__":
	main()

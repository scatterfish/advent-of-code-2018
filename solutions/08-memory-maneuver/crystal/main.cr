
struct Node
    property child_count    : UInt32 = 0
    property metadata_count : UInt32 = 0
    property child_nodes    : Array(Node) = Array(Node).new
    property metadata       : Array(UInt32) = Array(UInt32).new
end

class NodeData # workaround for lack of globals
	class_property data : Array(UInt32) = File.read("input.txt").strip.split.map(&.to_u32).reverse
end

root = get_tree_from_data

puts "Metadata sum: #{get_metadata_sum(root)}"
puts "Root value: #{get_node_value(root)}"

def get_tree_from_data()
	node = Node.new
	node.metadata_count, node.child_count = NodeData.data.pop(2)
	if node.child_count != 0
		node.child_count.times do
			node.child_nodes << get_tree_from_data
		end
	end
	node.metadata_count.times do
		node.metadata << NodeData.data.pop
	end
	node
end

def get_metadata_sum(node)
	metadata_sum = node.metadata.sum
	if node.child_count == 0
		metadata_sum
	else
		metadata_sum + node.child_nodes.map { |n| get_metadata_sum(n).as(UInt32) }
		                               .sum
	end
end

def get_node_value(node)
	metadata_sum = node.metadata.sum
	if node.child_count == 0
		metadata_sum
	else
		node.metadata.reject { |i| i > node.child_count }
		             .map    { |i| get_node_value(node.child_nodes[i - 1]).as(UInt32) }
		             .sum
	end
end

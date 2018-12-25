
def bit(val : Bool) # convert bool to 0 or 1 as u32
	val ? 1_u32 : 0_u32
end

OPERATIONS = {
	"addr" => ->(a : UInt32, b : UInt32, c : UInt32, reg : Array(UInt32)) { reg[c] = reg[a] + reg[b] },
	"addi" => ->(a : UInt32, b : UInt32, c : UInt32, reg : Array(UInt32)) { reg[c] = reg[a] + b      },
	
	"mulr" => ->(a : UInt32, b : UInt32, c : UInt32, reg : Array(UInt32)) { reg[c] = reg[a] * reg[b] },
	"muli" => ->(a : UInt32, b : UInt32, c : UInt32, reg : Array(UInt32)) { reg[c] = reg[a] * b      },
	
	"banr" => ->(a : UInt32, b : UInt32, c : UInt32, reg : Array(UInt32)) { reg[c] = reg[a] & reg[b] },
	"bani" => ->(a : UInt32, b : UInt32, c : UInt32, reg : Array(UInt32)) { reg[c] = reg[a] & b      },
	
	"borr" => ->(a : UInt32, b : UInt32, c : UInt32, reg : Array(UInt32)) { reg[c] = reg[a] | reg[b] },
	"bori" => ->(a : UInt32, b : UInt32, c : UInt32, reg : Array(UInt32)) { reg[c] = reg[a] | b      },
	
	"setr" => ->(a : UInt32, b : UInt32, c : UInt32, reg : Array(UInt32)) { reg[c] = reg[a] },
	"seti" => ->(a : UInt32, b : UInt32, c : UInt32, reg : Array(UInt32)) { reg[c] = a      },
	
	"gtir" => ->(a : UInt32, b : UInt32, c : UInt32, reg : Array(UInt32)) { reg[c] = bit(a > reg[b])      },
	"gtri" => ->(a : UInt32, b : UInt32, c : UInt32, reg : Array(UInt32)) { reg[c] = bit(reg[a] > b)      },
	"gtrr" => ->(a : UInt32, b : UInt32, c : UInt32, reg : Array(UInt32)) { reg[c] = bit(reg[a] > reg[b]) },
	
	"eqir" => ->(a : UInt32, b : UInt32, c : UInt32, reg : Array(UInt32)) { reg[c] = bit(a == reg[b])      },
	"eqri" => ->(a : UInt32, b : UInt32, c : UInt32, reg : Array(UInt32)) { reg[c] = bit(reg[a] == b)      },
	"eqrr" => ->(a : UInt32, b : UInt32, c : UInt32, reg : Array(UInt32)) { reg[c] = bit(reg[a] == reg[b]) },
}

lines = File.read_lines("input.txt", chomp: true)

ip_reg = lines.shift[4..-1].to_u32

puts "Part 1 answer: #{run_program(lines, [0_u32] * 6, ip_reg)}"
puts "Part 2 answer: #{run_program(lines, [1_u32] + [0_u32] * 5, ip_reg)}"

REG_HARDCODE = 1 # not sure how to (at least somewhat) elegantly generalize this out

def run_program(instructions, reg, ip_reg)
	ip_val = 0_u32
	while 0 <= ip_val < instructions.size
		pieces = instructions[ip_val].split
		opname = pieces[0]
		a, b, c = pieces[1..-1].map(&.to_u32)
		reg[ip_reg] = ip_val
		OPERATIONS[opname].call(a, b, c, reg)
		ip_val = reg[ip_reg] + 1
		if ip_val == 1
			return (1..reg[REG_HARDCODE]).select { |i| reg[REG_HARDCODE] % i == 0 }
			                             .sum
		end
	end
end

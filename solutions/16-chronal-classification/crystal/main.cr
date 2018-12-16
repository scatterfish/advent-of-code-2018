
def bit(val : Bool) # convert bool to 0 or 1 as u32
	val ? 1_u32 : 0_u32
end

OPCODES = {
	:addr => ->(a : UInt32, b : UInt32, c : UInt32, reg : Array(UInt32)) { reg[c] = reg[a] + reg[b] },
	:addi => ->(a : UInt32, b : UInt32, c : UInt32, reg : Array(UInt32)) { reg[c] = reg[a] + b      },
	
	:mulr => ->(a : UInt32, b : UInt32, c : UInt32, reg : Array(UInt32)) { reg[c] = reg[a] * reg[b] },
	:muli => ->(a : UInt32, b : UInt32, c : UInt32, reg : Array(UInt32)) { reg[c] = reg[a] * b      },
	
	:banr => ->(a : UInt32, b : UInt32, c : UInt32, reg : Array(UInt32)) { reg[c] = reg[a] & reg[b] },
	:bani => ->(a : UInt32, b : UInt32, c : UInt32, reg : Array(UInt32)) { reg[c] = reg[a] & b      },
	
	:borr => ->(a : UInt32, b : UInt32, c : UInt32, reg : Array(UInt32)) { reg[c] = reg[a] | reg[b] },
	:bori => ->(a : UInt32, b : UInt32, c : UInt32, reg : Array(UInt32)) { reg[c] = reg[a] | b      },
	
	:setr => ->(a : UInt32, b : UInt32, c : UInt32, reg : Array(UInt32)) { reg[c] = reg[a] },
	:seti => ->(a : UInt32, b : UInt32, c : UInt32, reg : Array(UInt32)) { reg[c] = a      },
	
	:gtir => ->(a : UInt32, b : UInt32, c : UInt32, reg : Array(UInt32)) { reg[c] = bit(a > reg[b])      },
	:gtri => ->(a : UInt32, b : UInt32, c : UInt32, reg : Array(UInt32)) { reg[c] = bit(reg[a] > b)      },
	:gtrr => ->(a : UInt32, b : UInt32, c : UInt32, reg : Array(UInt32)) { reg[c] = bit(reg[a] > reg[b]) },
	
	:eqir => ->(a : UInt32, b : UInt32, c : UInt32, reg : Array(UInt32)) { reg[c] = bit(a == reg[b])      },
	:eqri => ->(a : UInt32, b : UInt32, c : UInt32, reg : Array(UInt32)) { reg[c] = bit(reg[a] == b)      },
	:eqrr => ->(a : UInt32, b : UInt32, c : UInt32, reg : Array(UInt32)) { reg[c] = bit(reg[a] == reg[b]) },
}

Candidates = OPCODES.keys.each_with_object({} of Symbol => Set(UInt32)) do |opname, candidates|
	candidates[opname] = Set(UInt32).new
end

ref, data = File.read("input.txt").split("\n\n\n\n").map(&.lines)

part_one_count = 0
ref.each_slice(4) do |block|
	
	reg_before      = block[0][9..18].split(", ").map(&.to_u32)
	opcode, a, b, c = block[1].split.map(&.to_u32)
	reg_after       = block[2][9..18].split(", ").map(&.to_u32)
	
	possibilites = [] of UInt32
	OPCODES.each do |name, op|
		test_reg = reg_before.clone
		op.call(a, b, c, test_reg)
		if test_reg == reg_after
			Candidates[name] << opcode
			possibilites << opcode
		end
	end
	part_one_count += 1 if possibilites.size >= 3
	
end

puts "Part 1 answer: #{part_one_count}"

OPCODE_MAP = Hash(UInt32, Proc(UInt32, UInt32, UInt32, Array(UInt32), UInt32)).new
while OPCODE_MAP.size < OPCODES.size
	Candidates.each do |opname, candidates|
		if candidates.size == 1
			opcode = Candidates[opname].first
			OPCODE_MAP[opcode] = OPCODES[opname]
			Candidates.each do |_, c|
				c.delete(opcode)
			end
		end
	end
end

reg = [0_u32] * 4
data.each do |line|
	opcode, a, b, c = line.split.map(&.to_u32)
	OPCODE_MAP[opcode].call(a, b, c, reg)
end

puts "Part 2 answer: #{reg.first}"

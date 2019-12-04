def evaluate_chunk(chunk, data):
	# Modifies its input!
	opcode = chunk[0]
	if opcode == 1:
		data[chunk[3]] = data[chunk[1]] + data[chunk[2]]
		return True
	elif opcode == 2:
		data[chunk[3]] = data[chunk[1]] * data[chunk[2]]
		return True
	elif opcode == 99:
		return False

def evalute_program(program):
	# Modifies its input!
	for i in range(0, len(program), 4):
		if not evaluate_chunk(program[i : i + 4], program):
			break

def part1():
	with open('input.txt', 'r') as f:
		program = [int(x) for x in f.read().split(',')]

	program[1] = 12
	program[2] = 2
	evalute_program(program)
	
	with open('output.txt', 'w') as f:
		f.write(','.join(map(str, program)))

def part2():
	with open('input.txt', 'r') as f:
		program = [int(x) for x in f.read().split(',')]

	magic_number = 19690720
	for noun in range(100):
		for verb in range(100):
			possible_program = program.copy()
			possible_program[1] = noun
			possible_program[2] = verb
			evalute_program(possible_program)
			if possible_program[0] == magic_number:
				print("Done!")
				print("Noun: {}; verb: {}; Solution: {}".format(noun, verb, 100 * noun + verb))


if __name__ == '__main__':
	part1()
	part2()
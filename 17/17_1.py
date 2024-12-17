example = False
debug = False

def op_value(value):
    if value <= 3:
        return value
    elif value == 4:
        return a
    elif value == 5:
        return b
    elif value == 6:
        return c

lines = open(f"17/{'ex' if example else 'in'}.txt", "r").readlines()

instructions = ["adv: A = A // 2 ^ cop", "bxl: B = B xor lop", "bst: B = cop % 8", "jnz: jump to lop if A != 0", "bxc: B = B xor C", "out: output cop % 8", "bdv: B =  A // 2 ^ cop", "cdv: C = A // 2 ^ cop"]
operands = ["0", "1", "2", "3", "A or 4", "B or 5", "C or 6", "Reserved or 7"]

a = int(lines[0].split(" ")[2].strip())
b = int(lines[1].split(" ")[2].strip())
c = int(lines[2].split(" ")[2].strip())

program = [int(c) for c in lines[4].split(" ")[1].strip().split(",")]
pointer = 0
out = []

print(program)
while pointer < len(program):
    if debug:
        print("Pointer:", pointer)
        print("A: ", a, " B: ", b, " C: ", c)
        print("Instruction:", instructions[program[pointer]])
        print("Operand:", operands[program[pointer + 1]])
        print("----------")
    match program[pointer]:
        case 0:
            a = a // 2 ** op_value(program[pointer + 1])
        case 1:
            b = b ^ program[pointer + 1]
        case 2:
            b = op_value(program[pointer + 1]) % 8
        case 3:
            pointer = program[pointer + 1] - 2 if a != 0 else pointer
        case 4:
            b = b ^ c
        case 5:
            out.append(op_value(program[pointer + 1]) % 8) 
        case 6:
            b = a // 2 ** op_value(program[pointer + 1])
        case 7:
            c = a // 2 ** op_value(program[pointer + 1])
    pointer += 2

print(",".join([str(el) for el in out]))
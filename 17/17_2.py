example = False

def op_value(value):
    if value <= 3:
        return value
    elif value == 4:
        return a
    elif value == 5:
        return b
    elif value == 6:
        return c

lines = open(f"17/{'ex_2' if example else 'in'}.txt", "r").readlines()

program_str = lines[4].split(" ")[1].strip()
program = [int(c) for c in lines[4].split(" ")[1].strip().split(",")]

found = False
a = b = c = 0
fact = 2 ** (3 * (len(program) - 1))
curr_a = 3 * fact
lim = 8 * fact
print(curr_a, lim)

while not found and curr_a < lim:
    if curr_a % 1000000 == 0:
        print(curr_a)
    a = curr_a
    b = 0
    c = 0
    outp = 0
    pointer = 0
    out = []
    while pointer < len(program):
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
                if out[outp] != program[outp]:
                    break
                outp += 1
            case 6:
                b = a // 2 ** op_value(program[pointer + 1])
            case 7:
                c = a // 2 ** op_value(program[pointer + 1])
        pointer += 2
    res = ",".join([str(el) for el in out])
    if res == program_str:
        found = True
    else:
        curr_a += 1

print(curr_a)
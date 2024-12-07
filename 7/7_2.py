example = False
s = "ex" if example else "in"

def evaluate(result, numbers, ops):
    res = numbers[0]
    for i in range(len(ops)):
        if ops[i] == "+":
            res += numbers[i + 1]
        elif ops[i] == "*":
            res *= numbers[i + 1]
        elif ops[i] == "|":
            res = int(str(res) + str(numbers[i + 1]))
    return res == result

def check_operators(result, numbers, ops, index):
    if len(ops) == len(numbers) - 1:
        return evaluate(result, numbers, ops)
    for op in ["+", "*", "|"]:
        ops.append(op)
        if check_operators(result, numbers, ops, index + 1):
            return True
        ops.pop()
    return False

input = open(f"7/{s}.txt", "r")

equations = []

for line in input.readlines():
    parts = line.strip().split(":")
    equations.append((int(parts[0]), [int(i) for i in parts[1].strip().split(" ")]))

res = 0

for eq in equations:
    if(check_operators(eq[0], eq[1],[], 0)):
        res += eq[0]

print(res)
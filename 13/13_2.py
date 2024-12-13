from sympy.solvers import solve
from sympy import var, Eq
from sympy.core.numbers import int_valued

var('x y')

input = open(f"13/{'ex' if False else 'in'}.txt", "r")

def get_tokens(machine):
    eq1 = Eq(x*machine["a"][0] + y*machine["b"][0], machine["c"][0]) 
    eq2 = Eq(x*machine["a"][1] + y*machine["b"][1], machine["c"][1])
    output = solve([eq1, eq2], x, y, dict=True)
    if len(output) == 0 or not int_valued(output[0][x]) or not int_valued(output[0][y]):
        return 0
    return 3 * output[0][x] + output[0][y]

machines = []

input = input.readlines()
i = 0
while i < len(input):
    partsa = input[i].split(" ")
    a = (int(partsa[2][-3:-1]), int(partsa[3][-3:]))
    partsb = input[i + 1].split(" ")
    b = (int(partsb[2][-3:-1]), int(partsb[3][-3:]))
    partsc = input[i + 2].split(" ")
    c = (int(partsc[1][2:-1]) + 10000000000000, int(partsc[2][2:]) + 10000000000000)
    machines.append({"a": a, "b": b, "c": c})
    i += 4

tokens = 0

for machine in machines:
    tokens += get_tokens(machine)

print(tokens)

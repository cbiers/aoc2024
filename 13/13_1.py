input = open(f"13/{'ex' if False else 'in'}.txt", "r")

def get_tokens(machine):
    cand = []
    for i in range(101):
        for j in range (101):
            if machine["a"][0] * i + machine["b"][0] * j == machine["c"][0] and machine["a"][1] * i + machine["b"][1] * j == machine["c"][1]:
                cand.append(i * 3 + j)
    if len(cand) == 0:
        return 0
    return min(cand)

machines = []

input = input.readlines()
i = 0
while i < len(input):
    partsa = input[i].split(" ")
    a = (int(partsa[2][-3:-1]), int(partsa[3][-3:]))
    partsb = input[i + 1].split(" ")
    b = (int(partsb[2][-3:-1]), int(partsb[3][-3:]))
    partsc = input[i + 2].split(" ")
    c = (int(partsc[1][2:-1]), int(partsc[2][2:]))
    machines.append({"a": a, "b": b, "c": c})
    i += 4

tokens = 0

for machine in machines:
    tokens += get_tokens(machine)

print(tokens)
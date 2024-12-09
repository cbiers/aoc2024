example = False
s = "ex" if example else "in"

input = open(f"9/{s}.txt", "r")

def combine_dots(mem, i):
    lost = 0
    for block in range(len(mem) - 1, 1, -1):
        if mem[block][0] == ".":
            if mem[block - 1][0] == ".":
                mem[block - 1] = (".", mem[block - 1][1] + mem[block][1])
                mem.pop(block)
                if block <= i:
                    lost += 1
    return lost

free = False
curr = 0
memory = []

for c in input.readlines()[0].strip():
    if free:
        if int(c) > 0:
            memory.append((".", int(c)))
    else:
        memory.append((curr, int(c)))
        curr += 1
    free = not free

i = len(memory)

while i >= 0:
    i -= 1
    if memory[i][0] == ".":
        continue
    dot = 0  
    while dot <= i and (memory[dot][0] != "." or memory[dot][1] < memory[i][1]):
        dot += 1
    if dot < i:
        rem = memory[dot][1] - memory[i][1]
        memory[dot] = memory[i]
        memory[i] = (".", memory[i][1])
        if rem > 0:
            memory.insert(dot + 1, (".", rem))
            i += 1
        i -= combine_dots(memory, i)

res = 0
run = 0

for i in range(len(memory)):
    if memory[i][0] != ".":
        for j in range(run, run + memory[i][1]):
            res += memory[i][0] * j
    run += memory[i][1]

print(res)
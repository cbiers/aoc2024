example = False
s = "ex" if example else "in"

input = open(f"9/{s}.txt", "r")

free = False
curr = 0
nums = 0
memory = []

for c in input.readlines()[0].strip():
    if free:
        memory += "." * int(c)
    else:
        for i in range(int(c)):
            memory.append(str(curr))
        curr += 1
        nums += int(c)
    free = not free

dot = 0  
for i in range(len(memory) - 1, nums - 1, -1):
    while memory[dot] != ".":
        dot += 1
    memory[dot], memory[i] = memory[i], memory[dot]

res = 0

for i in range(len(memory)):
    if memory[i] == ".":
        break
    res += int(memory[i]) * i 

print(res)
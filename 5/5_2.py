example = False

def check_order(parts, i, rules):
    for j in range(i + 1, len(parts)):
        if parts[j] in rules:
            return False
    return True

def reorder(parts, rules):
    for i in range(len(parts)):
        curr = parts[i]
        if curr in rules.keys():
            for j in range(i + 1, len(parts)):
                if parts[j] in rules[curr]:
                    parts.insert(i, parts.pop(j))
    return parts

if example:
    s = "ex"
else:
    s = "in"

in1 = open(f"5/{s}.txt", "r")
lines1 = in1.readlines()

rules = {}

for line in lines1:
    parts = line.strip().split("|")
    if parts[1] not in rules:
        rules[parts[1]] = [parts[0]]
    else:
        rules[parts[1]].append(parts[0])

in2 = open(f"5/{s}_2.txt", "r")
lines2 = in2.readlines()

res = 0

for line in lines2:
    good = True
    parts = line.strip().split(",")
    for i in range(len(parts)):
        if parts[i] in rules:
            check = check_order(parts, i, rules[parts[i]])
            if not check:
                good = False
                break    
    if not good:
        while not good:
            parts = reorder(parts, rules)
            good = True
            for i in range(len(parts)):
                if parts[i] in rules:
                    if not check_order(parts, i, rules[parts[i]]):
                        good = False
                        break
        res += int(parts[len(parts) // 2])

print(res)
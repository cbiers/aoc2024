example = False
s = "ex" if example else "in"

def reachable(map, start, end):
    if start == end:
        return True 
    candidates = [(start[0] + 1, start[1]), (start[0] - 1, start[1]), (start[0], start[1] + 1), (start[0], start[1] - 1)]
    for candidate in candidates:
        if not(candidate[0] < 0 or candidate[0] >= len(map) or candidate[1] < 0 or candidate[1] >= len(map[0])):
            if map[candidate[0]][candidate[1]] == map[start[0]][start[1]] + 1:
                if reachable(map, candidate, end):
                    return True
    return False

input = open(f"10/{s}.txt", "r")

map = []
zeroes = []
nines = []

for line in input.readlines():
    map.append([])
    for c in line.strip():
        map[-1].append(int(c))
        if c == "0":
            zeroes.append((len(map) - 1, len(map[-1]) - 1))
        elif c == "9":
            nines.append((len(map) - 1, len(map[-1]) - 1))

res = 0

for zero in zeroes:
    for nine in nines:
        if reachable(map, zero, nine):
            res += 1

print(res)
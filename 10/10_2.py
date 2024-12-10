example = False
s = "ex" if example else "in"

def count_trails(map, pos):
    if map[pos[0]][pos[1]] == 9:
        return 1
    res = 0
    candidates = [(pos[0] + 1, pos[1]), (pos[0] - 1, pos[1]), (pos[0], pos[1] + 1), (pos[0], pos[1] - 1)]
    for candidate in candidates:
        if not(candidate[0] < 0 or candidate[0] >= len(map) or candidate[1] < 0 or candidate[1] >= len(map[0])):
            if map[candidate[0]][candidate[1]] == map[pos[0]][pos[1]] + 1:
                res += count_trails(map, candidate)
    return res

input = open(f"10/{s}.txt", "r")

map = []
zeroes = []

for line in input.readlines():
    map.append([])
    for c in line.strip():
        map[-1].append(int(c))
        if c == "0":
            zeroes.append((len(map) - 1, len(map[-1]) - 1))

res = 0

for zero in zeroes:
    res += count_trails(map, zero)

print(res)
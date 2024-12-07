example = False
s = "ex" if example else "in"

input = open(f"6/{s}.txt", "r")

map = []

for line in input.readlines():
    map.append([c for c in line.strip()]) 

visited = [[False for _ in range(len(map[0]))] for _ in range(len(map))]

for line in map:
    for c in line:
        if c == "^":
            pos = (map.index(line), line.index(c))

visited[pos[0]][pos[1]] = True
dir = "^"

while pos[0] >= 0 and pos[0] <= len(map) - 1 and pos[1] >= 0 and pos[1] <= len(map[0]) - 1:
    if dir == "^":
        if pos[0] > 0 and map[pos[0] - 1][pos[1]] == "#":
            dir = ">"
        else:
            pos = (pos[0] - 1, pos[1])
            if pos[0] >= 0:
                visited[pos[0]][pos[1]] = True
    elif dir == "v":
        if pos[0] < len(map) - 1 and map[pos[0] + 1][pos[1]] == "#":
            dir = "<"
        else:
            pos = (pos[0] + 1, pos[1])
            if pos[0] <= len(map) - 1:
                visited[pos[0]][pos[1]] = True
    elif dir == "<":
        if pos[1] > 0 and map[pos[0]][pos[1] - 1] == "#":
            dir = "^"
        else:
            pos = (pos[0], pos[1] - 1)
            if pos[1] >= 0:
                visited[pos[0]][pos[1]] = True
    elif dir == ">":
        if pos[1] < len(map[0]) - 1 and map[pos[0]][pos[1] + 1] == "#":
            dir = "v"
        else:
            pos = (pos[0], pos[1] + 1)
            if pos[1] <= len(map[0]) - 1:
                visited[pos[0]][pos[1]] = True

print(sum([v.count(True) for v in visited]))

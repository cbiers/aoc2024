import copy

example = False
s = "ex" if example else "in"

input = open(f"6/{s}.txt", "r")

initmap = []

for line in input.readlines():
    initmap.append([c for c in line.strip()]) 

for line in initmap:
    for c in line:
        if c == "^":
            initpos = (initmap.index(line), line.index(c))

initmap[initpos[0]][initpos[1]] = "^"

count = 0

for i in range(len(initmap)):
    for j in range(len(initmap[0])):
        if initmap[i][j] == "#" or initmap[i][j] == "^":
            continue

        map = copy.deepcopy(initmap)
        map[i][j] = "#"
        dir = "^"
        curr = []
        pos = initpos

        while pos[0] >= 0 and pos[0] <= len(map) - 1 and pos[1] >= 0 and pos[1] <= len(map[0]) - 1:
            if (pos[0], pos[1], dir) in curr:
                count += 1
                break
            else:
                curr.append((pos[0], pos[1], dir))
            if dir == "^":
                if pos[0] > 0 and map[pos[0] - 1][pos[1]] == "#":
                    dir = ">"
                else:
                    pos = (pos[0] - 1, pos[1])
                    if pos[0] >= 0:
                        map[pos[0]][pos[1]] = ">"
            elif dir == "v":
                if pos[0] < len(map) - 1 and map[pos[0] + 1][pos[1]] == "#":
                    dir = "<"
                else:
                    pos = (pos[0] + 1, pos[1])
                    if pos[0] <= len(map) - 1:
                        map[pos[0]][pos[1]] = "<"
            elif dir == "<":
                if pos[1] > 0 and map[pos[0]][pos[1] - 1] == "#":
                    dir = "^"
                else:
                    pos = (pos[0], pos[1] - 1)
                    if pos[1] >= 0:
                        map[pos[0]][pos[1]] = "^"
            elif dir == ">":
                if pos[1] < len(map[0]) - 1 and map[pos[0]][pos[1] + 1] == "#":
                    dir = "v"
                else:
                    pos = (pos[0], pos[1] + 1)
                    if pos[1] <= len(map[0]) - 1:
                        map[pos[0]][pos[1]] = "v"

print(count)
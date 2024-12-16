example = False

input_map = open(f"15/map_{'ex' if example else 'in'}.txt", "r")
input_moves = open(f"15/move_{'ex' if example else 'in'}.txt", "r")

moves = [c for c in input_moves.readline()]

m = {"boxes": [], "walls": []}

lines = input_map.readlines()
height = len(lines)
width = len(lines[0]) - 1
for i in range(len(lines)):
    for j in range(len(lines[i])):
        if lines[i][j] == "#":
            m["walls"].append((i, j))
        elif lines[i][j] == "O":
            m["boxes"].append((i, j))
        elif lines[i][j] == "@":
            m["robot"] = (i, j)

for move in moves:
    if move == "^":
        if (m["robot"][0] - 1, m["robot"][1]) in m["walls"]:
            continue
        elif (m["robot"][0] - 1, m["robot"][1]) in m["boxes"]:
            moved = False
            for i in range(m["robot"][0] - 1, 0, -1):
                if (i, m["robot"][1]) in m["walls"]:
                    break
                if (i, m["robot"][1]) not in m["boxes"]:
                    m["boxes"].remove((m["robot"][0] - 1, m["robot"][1]))
                    m["boxes"].append((i, m["robot"][1]))
                    moved = True
                    break
            if moved:
                m["robot"] = (m["robot"][0] - 1, m["robot"][1])
        else:
            m["robot"] = (m["robot"][0] - 1, m["robot"][1])
    elif move == "v":
        if (m["robot"][0] + 1, m["robot"][1]) in m["walls"]:
            continue
        elif (m["robot"][0] + 1, m["robot"][1]) in m["boxes"]:
            moved = False
            for i in range(m["robot"][0] + 1, len(lines)):
                if (i, m["robot"][1]) in m["walls"]:
                    break
                if (i, m["robot"][1]) not in m["boxes"]:
                    m["boxes"].remove((m["robot"][0] + 1, m["robot"][1]))
                    m["boxes"].append((i, m["robot"][1]))
                    moved = True
                    break
            if moved:
                m["robot"] = (m["robot"][0] + 1, m["robot"][1])
        else:
            m["robot"] = (m["robot"][0] + 1, m["robot"][1])
    elif move == "<":
        if (m["robot"][0], m["robot"][1] - 1) in m["walls"]:
            continue
        elif (m["robot"][0], m["robot"][1] - 1) in m["boxes"]:
            moved = False
            for i in range(m["robot"][1] - 1, 0, -1):
                if (m["robot"][0], i) in m["walls"]:
                    break
                if (m["robot"][0], i) not in m["boxes"]:
                    m["boxes"].remove((m["robot"][0], m["robot"][1] - 1))
                    m["boxes"].append((m["robot"][0], i))
                    moved = True
                    break
            if moved:
                m["robot"] = (m["robot"][0], m["robot"][1] - 1)
        else:   
            m["robot"] = (m["robot"][0], m["robot"][1] - 1)
    else:
        if (m["robot"][0], m["robot"][1] + 1) in m["walls"]:
            continue
        elif (m["robot"][0], m["robot"][1] + 1) in m["boxes"]:
            moved = False
            for i in range(m["robot"][1] + 1, len(lines[0])):
                if (m["robot"][0], i) in m["walls"]:
                    break
                if (m["robot"][0], i) not in m["boxes"]:
                    m["boxes"].remove((m["robot"][0], m["robot"][1] + 1))
                    m["boxes"].append((m["robot"][0], i))
                    moved = True
                    break
            if moved:
                m["robot"] = (m["robot"][0], m["robot"][1] + 1)
        else:
            m["robot"] = (m["robot"][0], m["robot"][1] + 1)

res = 0

for box in m["boxes"]:
    res += 100 * box[0] + box[1]

print(res)
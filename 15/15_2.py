example = False

input_map = open(f"15/map_{'ex' if example else 'in'}.txt", "r")
input_moves = open(f"15/move_{'ex' if example else 'in'}.txt", "r")

def move_up():
    to_test = [(m["robot"][0] - 1, m["robot"][1])]
    tested = [m["robot"]]
    while len(to_test) > 0:
        if to_test[0] in m["walls"]:
            return
        if to_test[0] in m["lboxes"]:
            tested.append(to_test[0])
            if (to_test[0][0], to_test[0][1] + 1) not in tested:
                to_test.append((to_test[0][0], to_test[0][1] + 1))
            if (to_test[0][0] - 1, to_test[0][1]) not in tested:
                to_test.append((to_test[0][0] - 1, to_test[0][1]))
        elif to_test[0] in m["rboxes"]:
            tested.append(to_test[0])
            if (to_test[0][0], to_test[0][1] - 1) not in tested:
                to_test.append((to_test[0][0], to_test[0][1] - 1))
            if (to_test[0][0] - 1, to_test[0][1]) not in tested:
                to_test.append((to_test[0][0] - 1, to_test[0][1]))
        to_test.pop(0)
    currl = m["lboxes"][:]
    currr = m["rboxes"][:]
    for c in set(tested):
        if c in currl:
            m["lboxes"].remove(c)
            m["lboxes"].append((c[0] - 1, c[1]))
        elif c in currr:
            m["rboxes"].remove(c)
            m["rboxes"].append((c[0] - 1, c[1]))
        elif c == m["robot"]:
            m["robot"] = (c[0] - 1, c[1])
        
def move_down():
    to_test = [(m["robot"][0] + 1, m["robot"][1])]
    tested = [m["robot"]]
    while len(to_test) > 0:
        if to_test[0] in m["walls"]:
            return
        if to_test[0] in m["lboxes"]:
            tested.append(to_test[0])
            if (to_test[0][0] + 1, to_test[0][1]) not in tested:
                to_test.append((to_test[0][0] + 1, to_test[0][1]))
            if (to_test[0][0], to_test[0][1] + 1) not in tested:
                to_test.append((to_test[0][0], to_test[0][1] + 1))
        elif to_test[0] in m["rboxes"]:
            tested.append(to_test[0])
            if (to_test[0][0] + 1, to_test[0][1]) not in tested:
                to_test.append((to_test[0][0] + 1, to_test[0][1]))
            if (to_test[0][0], to_test[0][1] - 1) not in tested:
                to_test.append((to_test[0][0], to_test[0][1] - 1))
        to_test.pop(0)
    currl = m["lboxes"][:]
    currr = m["rboxes"][:]
    for c in set(tested):
        if c in currl:
            m["lboxes"].remove(c)
            m["lboxes"].append((c[0] + 1, c[1]))
        elif c in currr:
            m["rboxes"].remove(c)
            m["rboxes"].append((c[0] + 1, c[1]))
        elif c == m["robot"]:
            m["robot"] = (c[0] + 1, c[1])

def move_left():
    for i in range(m["robot"][1] - 1, 0, -1):
        if (m["robot"][0], i) in m["walls"]:
            return
        if (m["robot"][0], i) not in m["lboxes"] and (m["robot"][0], i) not in m["rboxes"]:
            for j in range(i, m["robot"][1]):
                if (m["robot"][0], j) in m["lboxes"]:
                    m["lboxes"].remove((m["robot"][0], j))
                    m["lboxes"].append((m["robot"][0], j - 1))
                elif (m["robot"][0], j) in m["rboxes"]:
                    m["rboxes"].remove((m["robot"][0], j))
                    m["rboxes"].append((m["robot"][0], j - 1))
            m["robot"] = (m["robot"][0], m["robot"][1] - 1)
            return

def move_right():
    for i in range(m["robot"][1] + 1, 2 * width):
        if (m["robot"][0], i) in m["walls"]:
            return
        if (m["robot"][0], i) not in m["lboxes"] and (m["robot"][0], i) not in m["rboxes"]:
            for j in range(i, m["robot"][1], -1):
                if (m["robot"][0], j) in m["lboxes"]:
                    m["lboxes"].remove((m["robot"][0], j))
                    m["lboxes"].append((m["robot"][0], j + 1))
                elif (m["robot"][0], j) in m["rboxes"]:
                    m["rboxes"].remove((m["robot"][0], j))
                    m["rboxes"].append((m["robot"][0], j + 1))
            m["robot"] = (m["robot"][0], m["robot"][1] + 1)
            return

moves = [c for c in input_moves.readline()]

m = {"lboxes": [], "rboxes": [], "walls": []}

lines = input_map.readlines()
height = len(lines)
width = len(lines[0]) - 1
for i in range(len(lines)):
    for j in range(len(lines[i])):
        if lines[i][j] == "#":
            m["walls"].append((i, 2 * j))
            m["walls"].append((i, 2 * j + 1))
        elif lines[i][j] == "O":
            m["lboxes"].append((i, 2 * j))
            m["rboxes"].append((i, 2 * j + 1))
        elif lines[i][j] == "@":
            m["robot"] = (i, 2 * j)

for move in moves:
    if move == "^":
        move_up()
    elif move == "v":
        move_down()
    elif move == "<":
        move_left()
    else:
        move_right()

res = 0

for box in m["lboxes"]:
    res += 100 * box[0] + box[1]

print(res)
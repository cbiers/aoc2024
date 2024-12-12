input = open(f"12/{'ex' if False else 'in'}.txt", "r")

map = []
lines = input.readlines()

for i in range(len(lines)):
    map.append([])
    for j in range(len(lines[i])):
        if lines[i][j] != "\n":
            map[i].append(lines[i][j])

shapes = []
visited = []

for i in range(len(map)):
    for j in range(len(map[i])):
        if(i, j) in visited:
            continue
        val = map[i][j]
        shapes.append([(i, j)])
        fringe = []
        visited.append((i, j))
        if i > 0 and map[i - 1][j] == val:
            fringe.append((i - 1, j))
        if i < len(map) - 1 and map[i + 1][j] == val:
            fringe.append((i + 1, j))
        if j > 0 and map[i][j - 1] == val:
            fringe.append((i, j - 1))
        if j < len(map[i]) - 1 and map[i][j + 1] == val:
            fringe.append((i, j + 1))
        while len(fringe) > 0:
            (a, b) = fringe.pop()
            visited.append((a, b))
            shapes[-1].append((a, b))
            if a > 0 and map[a - 1][b] == val and (a - 1, b) not in visited:
                fringe.append((a - 1, b))
            if a < len(map) - 1 and map[a + 1][b] == val and (a + 1, b) not in visited:
                fringe.append((a + 1, b))
            if b > 0 and map[a][b - 1] == val and (a, b - 1) not in visited:
                fringe.append((a, b - 1))
            if b < len(map[a]) - 1 and map[a][b + 1] == val and (a, b + 1) not in visited:
                fringe.append((a, b + 1))

counts = []

for i in range(len(map)):
    counts.append([])
    for j in range(len(map[i])):
        counts[i].append(0)
        if i == 0 or i > 0 and map[i - 1][j] != map[i][j]:
            counts[i][j] += 1
        if i == len(map) - 1 or i < len(map) - 1 and map[i + 1][j] != map[i][j]:
            counts[i][j] += 1
        if j == 0 or j > 0 and map[i][j - 1] != map[i][j]:
            counts[i][j] += 1
        if j == len(map[i]) - 1 or j < len(map[i]) - 1 and map[i][j + 1] != map[i][j]:
            counts[i][j] += 1
            
shape_counts = []

for i in range(len(shapes)):
    shapes[i] = set(shapes[i])

for shape in shapes:
    shape_counts.append(0)
    for (i, j) in shape:
        shape_counts[-1] += counts[i][j]
        
shape_lengths = [len(shape) for shape in shapes]

print(sum(c * l for c, l in zip(shape_counts, shape_lengths)))
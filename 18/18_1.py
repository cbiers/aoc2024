example = False
lines = open(f"18/{'ex' if example else 'in'}.txt", "r").readlines()

size = 9 if example else 73
start = (1, 1)
goal = (size - 2, size - 2)
lim = 12 if example else 1024

grid = [["." if i != 0 and j != 0 and i != size - 1 and j != size -1 else "#" for i in range(size)] for j in range(size)]

for line in lines[:lim]:
    parts = line.strip().split(",")
    grid[int(parts[1]) + 1][int(parts[0]) + 1] = "#"

for line in grid:
    print("".join(line))

def shortest_path(grid, start, end):
    queue = [(start, 0)]
    visited = set()
    while queue:
        (x, y), dist = queue.pop(0)
        if (x, y) == end:
            return dist
        if (x, y) in visited:
            continue
        visited.add((x, y))
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            new_x, new_y = x + dx, y + dy
            if grid[new_x][new_y] == ".":
                queue.append(((new_x, new_y), dist + 1))
    return -1

print(shortest_path(grid, start, goal))
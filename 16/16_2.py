example = True

lines = open(f"16/{'ex' if example else 'in'}.txt", "r").readlines()

maze = []

for i in range(len(lines)):
    maze.append([])
    for j in range(len(lines[i]) - 1):
        maze[i].append(lines[i][j])
        if lines[i][j] == "S":
            start = (i, j)
        if lines[i][j] == "E":
            end = (i, j)

move_cost, turn_cost = 1, 1000
N, E, S, W = 0, 1, 2, 3

def turn_left(dir):
    return (dir - 1) % 4
    
def turn_right(dir):
    return (dir + 1) % 4
    
def move_forward(pos, dir):
    return (pos[0] + (dir == S) - (dir == N), pos[1] + (dir == E) - (dir == W))

def bfs_with_costs(map, start, end, dir):
    costs = [[[1000000 for i in range(4)] for j in range(len(maze[0]))] for k in range(len(maze))]
    costs[start[0]][start[1]][dir] = 0
    queue = [(start, dir, 0)]
    visited = {}
    while len(queue) > 0:
        pos, dir, cost = queue.pop(0)
        if (pos, dir) in visited and visited[(pos, dir)] < cost:
            continue
        visited[(pos, dir)] = cost
        new_pos = move_forward(pos, dir)
        if map[new_pos[0]][new_pos[1]] != "#":
            if costs[new_pos[0]][new_pos[1]][dir] > cost + move_cost:
                costs[new_pos[0]][new_pos[1]][dir] = cost + move_cost
            queue.append((new_pos, dir, cost + move_cost))
        if costs[pos[0]][pos[1]][turn_left(dir)] > cost + turn_cost:
            costs[pos[0]][pos[1]][turn_left(dir)] = cost + turn_cost
        queue.append((pos, turn_left(dir), cost + turn_cost))
        if costs[pos[0]][pos[1]][turn_right(dir)] > cost + turn_cost:
            costs[pos[0]][pos[1]][turn_right(dir)] = cost + turn_cost
        queue.append((pos, turn_right(dir), cost + turn_cost))   
    return costs
       
costs = bfs_with_costs(maze, start, end, N)
costs2 = bfs_with_costs(maze, end, start, S)
totalcosts = [[min(costs[i][j][k] + costs2[i][j][k] for k in range(4)) for j in range(len(maze[0]))] for i in range(len(maze))]

points = set()
points.add(start)
points.add(end)

for i in range(len(maze)):
    for j in range(len(maze[0])):
        if totalcosts[i][j] == costs2[start[0]][start[1]][S]:
            points.add((i, j))    

for point in list(points):
    for point2 in list(points):
        if point != point2:
            if point[0] == point2[0]:
                if "#" not in [maze[point[0]][i] for i in range(min(point[1], point2[1]), max(point[1], point2[1]) + 1)]:
                    for i in range(min(point[1], point2[1]), max(point[1], point2[1]) + 1):
                            points.add((point[0], i))
            if point[1] == point2[1]:
                if "#" not in [maze[i][point[1]] for i in range(min(point[0], point2[0]), max(point[0], point2[0]) + 1)]:
                    for i in range(min(point[0], point2[0]), max(point[0], point2[0]) + 1):
                            points.add((i, point[1]))

print(len(points))
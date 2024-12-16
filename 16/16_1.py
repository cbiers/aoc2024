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

def dijkstra_with_turn_costs(maze, start, end, dir):
    best = 10000000
    costs = [[[10000000 for i in range(len(maze[0]))] for j in range(len(maze))] for dir in [N, E, S, W]]
    costs[E][start[0]][start[1]] = 0
    queue = [(start, E)]
    while len(queue) > 0:
        current = queue.pop(0)
        if current[0] == end:
            best = min(costs[current[1]][current[0][0]][current[0][1]], best)
        forward_pos = move_forward(current[0], current[1])
        if maze[forward_pos[0]][forward_pos[1]] != "#":
            if costs[current[1]][forward_pos[0]][forward_pos[1]] > costs[current[1]][current[0][0]][current[0][1]] + move_cost:
                costs[current[1]][forward_pos[0]][forward_pos[1]] = costs[current[1]][current[0][0]][current[0][1]] + move_cost
                queue.append((forward_pos, current[1]))
        if costs[turn_left(current[1])][current[0][0]][current[0][1]] > costs[current[1]][current[0][0]][current[0][1]] + turn_cost:
            costs[turn_left(current[1])][current[0][0]][current[0][1]] = costs[current[1]][current[0][0]][current[0][1]] + turn_cost
            queue.append((current[0], turn_left(current[1])))
        if costs[turn_right(current[1])][current[0][0]][current[0][1]] > costs[current[1]][current[0][0]][current[0][1]] + turn_cost:
            costs[turn_right(current[1])][current[0][0]][current[0][1]] = costs[current[1]][current[0][0]][current[0][1]] + turn_cost
            queue.append((current[0], turn_right(current[1])))
    return best

print(dijkstra_with_turn_costs(maze, start, end, dir))
example = False
input = open(f"10/{'ex' if example else 'in'}.txt", "r")

def count_trails(m, p):
    return 1 if m[p[0]][p[1]] == 9 else sum(count_trails(m, c) 
    for c in [(p[0] + 1, p[1]), (p[0] - 1, p[1]), (p[0], p[1] + 1), (p[0], p[1] - 1)] 
    if c[0] >= 0 and c[0] < len(m) and c[1] >= 0 and c[1] < len(m[0]) and m[c[0]][c[1]] == m[p[0]][p[1]] + 1)

m = [[int(c) for c in line.strip()] for line in input.readlines()]
zeroes = [(i, j) for i in range(len(m)) for j in range(len(m[0])) if m[i][j] == 0]

print(sum([count_trails(m, zero) for zero in zeroes]))
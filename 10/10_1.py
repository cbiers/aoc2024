example = False
input = open(f"10/{'ex' if example else 'in'}.txt", "r")

def reachable(m, s, e):
    return s == e or any([reachable(m, c, e) 
    for c in [(s[0] + i, s[1] + j) for i, j in [(1, 0), (-1, 0), (0, 1), (0, -1)]]
    if 0 <= c[0] < len(m) and 0 <= c[1] < len(m[0]) and m[c[0]][c[1]] == m[s[0]][s[1]] + 1])

m = [[int(c) for c in line.strip()] for line in input.readlines()]
zeroes = [(i, j) for i in range(len(m)) for j in range(len(m[0])) if m[i][j] == 0]
nines = [(i, j) for i in range(len(m)) for j in range(len(m[0])) if m[i][j] == 9]

print([reachable(m, zero, nine) for zero in zeroes for nine in nines].count(True))
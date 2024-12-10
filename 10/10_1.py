def reachable(m, s, e):
    return s == e or any([reachable(m, c, e) 
    for c in [(s[0] + i, s[1] + j) for i, j in [(1, 0), (-1, 0), (0, 1), (0, -1)]]
    if 0 <= c[0] < len(m) and 0 <= c[1] < len(m[0]) and m[c[0]][c[1]] == m[s[0]][s[1]] + 1])

def all_nums(m, n):
    return [(i, j) for i in range(len(m)) for j in range(len(m[0])) if m[i][j] == n]

m = [[int(c) for c in line.strip()] for line in open(f"10/{'ex' if False else 'in'}.txt", "r").readlines()]

print([reachable(m, zero, nine) for zero in all_nums(m, 0) for nine in all_nums(m, 9)].count(True))
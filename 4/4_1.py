input = open("4/in.txt", "r")
lines = input.readlines()

res = 0

for i in range(len(lines)):
    for j in range(len(lines[i]) - 1):
        if j < len(lines[i]) - 4:
            if lines[i][j] == "X" and lines[i][j + 1] == "M" and lines[i][j + 2] == "A" and lines[i][j + 3] == "S":
                res += 1
            if i < len(lines) - 3:
                if lines[i][j] == "X" and lines[i + 1][j + 1] == "M" and lines[i + 2][j + 2] == "A" and lines[i + 3][j + 3] == "S":
                    res += 1
            if i > 2:
                if lines[i][j] == "X" and lines[i - 1][j + 1] == "M" and lines[i - 2][j + 2] == "A" and lines[i - 3][j + 3] == "S":
                    res += 1
        if j > 2:
            if lines[i][j] == "X" and lines[i][j - 1] == "M" and lines[i][j - 2] == "A" and lines[i][j - 3] == "S":
                res += 1
            if i < len(lines) - 3:
                if lines[i][j] == "X" and lines[i + 1][j - 1] == "M" and lines[i + 2][j - 2] == "A" and lines[i + 3][j - 3] == "S":
                    res += 1
            if i > 2:
                if lines[i][j] == "X" and lines[i - 1][j - 1] == "M" and lines[i - 2][j - 2] == "A" and lines[i - 3][j - 3] == "S":
                    res += 1
        if i < len(lines) - 3:
            if lines[i][j] == "X" and lines[i + 1][j] == "M" and lines[i + 2][j] == "A" and lines[i + 3][j] == "S":
                res += 1
        if i > 2:
            if lines[i][j] == "X" and lines[i - 1][j] == "M" and lines[i - 2][j] == "A" and lines[i - 3][j] == "S":
                res += 1
        
print(res)
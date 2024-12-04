input = open("4/in.txt", "r")
lines = input.readlines()

res = 0

for i in range(1, len(lines) - 1):
    for j in range(1, len(lines[i]) - 1):
        mas = 0
        if lines[i][j] == "A":
            if lines[i - 1][j - 1] == "M" and lines[i + 1][j + 1] == "S":
                mas += 1
            if lines[i + 1][j + 1] == "M" and lines[i - 1][j - 1] == "S":
                mas += 1
            if lines[i - 1][j + 1] == "M" and lines[i + 1][j - 1] == "S":
                mas += 1
            if lines[i + 1][j - 1] == "M" and lines[i - 1][j + 1] == "S":
                mas += 1
            if mas == 2:
                res += 1
       
print(res)
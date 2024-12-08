example = False
s = "ex" if example else "in"

input = open(f"8/{s}.txt", "r")

lines = input.readlines()
width =  len(lines[0].strip())
height = len(lines)

antennas = {}
antinodes = set()

for i in range(height):
    for j in range(width):
        if lines[i][j] != ".":
            if lines[i][j] in antennas:
                antennas[lines[i][j]].append((i,j))
            else:
                antennas[lines[i][j]] = [(i,j)]

for type in antennas:
    for i in range(len(antennas[type]) - 1):
        for j in range(i + 1, len(antennas[type])):
            deltay = antennas[type][j][0] - antennas[type][i][0]
            deltax = antennas[type][j][1] - antennas[type][i][1]
            if antennas[type][i][0] - deltay >= 0 and antennas[type][i][1] - deltax >= 0 and antennas[type][i][0] - deltay < height and antennas[type][i][1] - deltax < width:
                antinodes.add((antennas[type][i][0] - deltay, antennas[type][i][1] - deltax))
            if antennas[type][j][0] + deltay < height and antennas[type][j][1] + deltax < width and antennas[type][j][0] + deltay >= 0 and antennas[type][j][1] + deltax >= 0:
                antinodes.add((antennas[type][j][0] + deltay, antennas[type][j][1] + deltax))

print(len(antinodes))
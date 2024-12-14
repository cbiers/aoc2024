example = False

input = open(f"14/{'ex' if example else 'in'}.txt", "r")
out = open("out.txt", "w")

robots = []

width = 11 if example else 101
height = 7 if example else 103

for line in input.readlines():
    parts = line.split(" ")
    posparts = parts[0].split(",")
    pos = (int(posparts[0][posparts[0].index("=") + 1:]), int(posparts[1]))
    velparts = parts[1].split(",")
    vel = (int(velparts[0][velparts[0].index("=") + 1:]) + width, int(velparts[1]) + height)
    robots.append({"pos": pos, "vel": vel})    

for i in range(1, 10000):
    out.write("-------------------\n")
    out.write(f"Iteration {i}\n")
    out.write("-------------------\n")
    for robot in robots:
        robot["pos"] = ((robot["pos"][0] + robot["vel"][0]) % width, (robot["pos"][1] + robot["vel"][1]) % height)
    for i in range(height):
        for j in range(width):
            if (j, i) in map(lambda robot: robot["pos"], robots):
                out.write("#")
            else:
                out.write(".")
        out.write("\n")

out.close()


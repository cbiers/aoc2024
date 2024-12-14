example = False

input = open(f"14/{'ex' if example else 'in'}.txt", "r")

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

for i in range(100):
    for robot in robots:
        robot["pos"] = ((robot["pos"][0] + robot["vel"][0]) % width, (robot["pos"][1] + robot["vel"][1]) % height)

print(robots)

q1 = list(filter(lambda robot: robot["pos"][0] < width // 2 and robot["pos"][1] < height // 2, robots))
q2 = list(filter(lambda robot: robot["pos"][0] > width // 2 and robot["pos"][1] < height // 2, robots))
q3 = list(filter(lambda robot: robot["pos"][0] < width // 2 and robot["pos"][1] > height // 2, robots))
q4 = list(filter(lambda robot: robot["pos"][0] > width // 2 and robot["pos"][1] > height // 2, robots))

print(len(q1) * len(q2) * len(q3) * len(q4))
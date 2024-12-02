def tryRemove(r):
    for i in range(len(r)):
        newR = r[:i] + r[i + 1:]
        good = True
        for j in range(len(newR) - 1):
            if int(newR[j + 1]) - int(newR[j]) > 3 or int(newR[j + 1]) - int(newR[j]) < 1:
                good = False
                break
        if good:
            return True

input = open('2/in.txt', 'r')
reports = [line.split() for line in input.readlines()]

res = 0

for report in reports:
    if int(report[0]) > int(report[-1]):
        report.reverse()

for report in reports:
    safe = True
    for i in range(len(report) - 1):
        if int(report[i + 1]) - int(report[i]) > 3 or int(report[i + 1]) - int(report[i]) < 1:
            safe = False
            break
    if safe or tryRemove(report):
        res += 1        

print(res)
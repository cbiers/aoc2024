input = open('1/in.txt', 'r')
lines = input.readlines()

l1 = [int(l[0]) for l in [line.split() for line in lines]]
l2 = [int(l[1]) for l in [line.split() for line in lines]]

occs1 = [0] * (max(max(l1), max(l2)) + 1)
occs2 = [0] * (max(max(l1), max(l2)) + 1)

for i in l1:
    occs1[i] += 1

for i in l2:
    occs2[i] += 1

res = 0

for i in range(len(occs1)):
    res += i * occs1[i] * occs2[i]

print(res)
input = open('1/in.txt', 'r')
lines = input.readlines()

l1 = [int(l[0]) for l in [line.split() for line in lines]]
l2 = [int(l[1]) for l in [line.split() for line in lines]]

l1.sort()
l2.sort()

res = sum([abs(a - b) for a, b in zip(l1, l2)])

print(res)

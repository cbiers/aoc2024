input = open('3/in2.txt', 'r')

res = 0
enabled = True

for line in input.readlines():
    for en in line.split("do()"):
        en2 = en.split("don't()")[0]
        for part in en2.split("mul("):
            if part.find(")") == -1:
                continue
            trimmed = part[:part.find(")")]
            nums = trimmed.split(",")
            if len(nums) == 2 and nums[0].isnumeric() and nums[1].isnumeric():
                res += int(nums[0]) * int(nums[1])
print(res)  
input = open('3/in.txt', 'r')

res = 0

for line in input.readlines():
    for part in line.split("mul("):
        trimmed = part[:part.find(")")]
        nums = trimmed.split(",")
        if len(nums) == 2 and nums[0].isnumeric() and nums[1].isnumeric():
            res += int(nums[0]) * int(nums[1])     

print(res)  
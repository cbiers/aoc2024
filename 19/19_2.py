example = False
lines = open(f"19/{'ex' if example else 'in'}.txt", "r").readlines()

def is_possible(pattern):
    if pattern in nope_cache:
        return False
    if pattern in cache or pattern == "":
        return True
    for stripe in stripes:
        if pattern.startswith(stripe) and is_possible(pattern[len(stripe):]):
            cache.add(pattern)
            return True
    nope_cache.add(pattern)
    return False

def combinations(pattern):
    if pattern in comb_cache:
        return comb_cache[pattern]
    if pattern == "":
        return 1
    res = 0
    for stripe in stripes:
        if pattern.startswith(stripe):
            res += combinations(pattern[len(stripe):])
    comb_cache[pattern] = comb_cache.get(pattern, 0) + res
    return res

stripes = lines[0].strip().split(", ")
cache = set()
nope_cache = set()
comb_cache = {}

count = 0

for line in lines[2:]:
    if is_possible(line.strip()):
        count += combinations(line.strip())

print(count)
example = False
lines = open(f"19/{'ex' if example else 'in'}.txt", "r").readlines()

def isPossible(pattern, stripes):
    if pattern in nope_cache:
        return False
    if pattern == "":
        return True
    possible = False
    for stripe in stripes:
        if pattern.startswith(stripe):
            if isPossible(pattern[len(stripe):], stripes):
                possible = True
                cache.add(pattern)
                break
    if possible == False:
        nope_cache.add(pattern)
    return possible

def combinations(pattern, stripes):
    if pattern in comb_cache:
        return comb_cache[pattern]
    if pattern == "":
        return 1
    res = 0
    for stripe in stripes:
        if pattern.startswith(stripe):
            res += combinations(pattern[len(stripe):], stripes)
    if pattern in comb_cache:
        comb_cache[pattern] += res
    else:
        comb_cache[pattern] = res
    return res

stripes = lines[0].strip().split(", ")
cache = set()
nope_cache = set()
comb_cache = {}

count = 0

for line in lines[2:]:
    if isPossible(line.strip(), stripes):
        count += combinations(line.strip(), stripes)

print(count)
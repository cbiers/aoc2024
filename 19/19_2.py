example = False
lines = open(f"19/{'ex' if example else 'in'}.txt", "r").readlines()

def is_possible(pattern):
    if pattern in cache:
        return cache[pattern]
    if pattern == "":
        cache[pattern] = True
        return True
    for stripe in stripes:
        if pattern.startswith(stripe) and is_possible(pattern[len(stripe):]):
            cache[pattern] = True
            return True
    cache[pattern] = False
    return False

def combinations(pattern):
    if pattern in comb_cache:
        return comb_cache[pattern]
    if pattern == "":
        return 1
    comb_cache[pattern] = sum([combinations(pattern[len(stripe):]) for stripe in stripes if pattern.startswith(stripe) and is_possible(pattern[len(stripe):])])
    return comb_cache[pattern]

stripes = lines[0].strip().split(", ")
patterns = [line.strip() for line in lines[2:]]
cache = {}
comb_cache = {}

print(sum(combinations(pattern) for pattern in patterns if is_possible(pattern)))
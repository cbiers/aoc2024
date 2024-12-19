example = False
lines = open(f"19/{'ex' if example else 'in'}.txt", "r").readlines()

def is_possible(pattern):
    if pattern not in cache:
        cache[pattern] = pattern == "" or any(pattern.startswith(stripe) and is_possible(pattern[len(stripe):]) for stripe in stripes)
    return cache[pattern]

def combinations(pattern):
    if pattern not in comb_cache:
        comb_cache[pattern] = sum(combinations(pattern[len(stripe):]) for stripe in stripes if pattern.startswith(stripe))
    return comb_cache[pattern]

stripes = lines[0].strip().split(", ")
patterns = [line.strip() for line in lines[2:]]
cache, comb_cache = {}, {"": 1}

print(sum(combinations(pattern) for pattern in patterns if is_possible(pattern)))
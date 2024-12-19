example = False
lines = open(f"19/{'ex' if example else 'in'}.txt", "r").readlines()

def is_possible(pattern):
    if pattern not in cache:
        cache[pattern] = pattern == "" or any(pattern.startswith(stripe) and is_possible(pattern[len(stripe):]) for stripe in stripes)
    return cache[pattern]

def combinations(pattern):
    if pattern not in comb_cache:
        comb_cache[pattern] = sum(combinations(pattern[len(stripe):]) for stripe in filter(pattern.startswith, stripes))
    return comb_cache[pattern]

stripes = lines[0].strip().split(", ")
cache, comb_cache = {}, {"": 1}

print(sum(combinations(pattern) for pattern in filter(is_possible, map(str.strip, lines[2:]))))
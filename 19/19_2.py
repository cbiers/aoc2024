example = False
file = map(str.strip, open(f"19/{'ex' if example else 'in'}.txt", "r"))

def is_possible(pattern):
    if pattern not in valid_cache:
        valid_cache[pattern] = pattern == "" or any(pattern.startswith(stripe) and is_possible(pattern[len(stripe):]) for stripe in stripes)
    return valid_cache[pattern]

def combinations(pattern):
    if pattern not in combination_cache:
        combination_cache[pattern] = sum(combinations(pattern[len(stripe):]) for stripe in filter(pattern.startswith, stripes))
    return combination_cache[pattern]

stripes = next(file).split(", ")
valid_cache, combination_cache = {}, {"": 1}

print(sum(combinations(pattern) for pattern in filter(is_possible, file)))
example = False
file = map(str.strip, open(f"19/{'ex' if example else 'in'}.txt", "r"))

def is_possible(pattern):
    if pattern not in cache:
        cache[pattern] = pattern == "" or any(pattern.startswith(stripe) and is_possible(pattern[len(stripe):]) for stripe in stripes)
    return cache[pattern]

stripes = next(file).split(", ")
cache = {}

print(sum(1 for pattern in filter(is_possible, file)))
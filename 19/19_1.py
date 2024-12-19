example = False
lines = open(f"19/{'ex' if example else 'in'}.txt", "r").readlines()

def is_possible(pattern):
    if pattern not in cache:
        cache[pattern] = pattern == "" or any(pattern.startswith(stripe) and is_possible(pattern[len(stripe):]) for stripe in stripes)
    return cache[pattern]

stripes = lines[0].strip().split(", ")
cache = {}

print(sum(1 for pattern in filter(is_possible, map(str.strip, lines[2:]))))
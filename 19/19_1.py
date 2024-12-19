example = False
lines = open(f"19/{'ex' if example else 'in'}.txt", "r").readlines()

def is_possible(pattern):
    if pattern in cache:
        return cache[pattern]
    cache[pattern] = pattern == "" or any(pattern.startswith(stripe) and is_possible(pattern[len(stripe):]) for stripe in stripes)
    return cache[pattern]

stripes = lines[0].strip().split(", ")
cache = {}

print(sum(is_possible(pattern.strip()) for pattern in lines[2:]))
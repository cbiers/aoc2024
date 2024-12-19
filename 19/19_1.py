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

stripes = lines[0].strip().split(", ")
cache = {}

print(sum(is_possible(pattern.strip()) for pattern in lines[2:]))
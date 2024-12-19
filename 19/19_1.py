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

stripes = lines[0].strip().split(", ")
cache = set()
nope_cache = set()

count = 0

for line in lines[2:]:
    if is_possible(line.strip()):
        count += 1

print(count)
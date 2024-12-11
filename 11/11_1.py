s = [int(c) for c in open(f"11/{'ex' if False else 'in'}.txt", "r").readlines()[0].strip().split(" ")]

def insert_and_strip(s, i, p):
    p.lstrip("0")
    if p == "":
        p = "0"
    s.insert(i, int(p))

for _ in range(25):
    i = len(s) - 1
    while i >= 0:
        if s[i] == 0:
            s[i] = 1
        elif len(str(s[i])) % 2 == 0:
            insert_and_strip(s, i + 1, str(s[i])[len(str(s[i])) // 2:])
            s[i] = int(str(s[i])[:len(str(s[i])) // 2])
        else:
            s[i] *= 2024  
        i -= 1

print(len(s))


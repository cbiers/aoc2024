s = {c : {"count": 1, "rep": None} for c in open(f"11/{'ex' if False else 'in'}.txt", "r").readlines()[0].strip().split(" ")}

for _ in range(75):
    add = []
    for v in [k for k in s if s[k]["count"] > 0]:
        if s[v]["rep"] == None:
            if v == "0":
                s[v]["rep"] = ["1"]
            elif len(v) % 2 == 0:
                s[v]["rep"] = [v[:len(v) // 2], v[len(v) // 2:].lstrip("0") if v[len(v) // 2:].lstrip("0") != "" else "0"]
            else:
                s[v]["rep"] = [str(int(v) * 2024)]
        c = s[v]["count"]
        s[v]["count"] = 0
        add.extend([(r, c) for r in s[v]["rep"]])
    for a in add:
        if a[0] in s:
            s[a[0]]["count"] += a[1]
        else:
            s[a[0]] = {"count": a[1], "rep": None}

print(sum(v["count"] for v in s.values()))
s = {c : {"count": 1, "rep": None} for c in open(f"11/{'ex' if False else 'in'}.txt", "r").readlines()[0].strip().split(" ")}

for j in range(75):
    add = []
    k = list(s.keys())
    for v in k:
        if s[v]["count"] == 0:
            continue
        if s[v]["rep"] == None:
            if v == "0":
                s[v]["rep"] = ["1"]
            elif len(v) % 2 == 0:
                sec = v[len(v) // 2:].lstrip("0")
                rep = [v[:len(v) // 2]] 
                if sec == "":
                    sec = "0"
                rep.append(sec)
                s[v]["rep"] = rep
            else:
                s[v]["rep"] = [str(int(v) * 2024)]
        c = s[v]["count"]
        s[v]["count"] = 0
        for r in s[v]["rep"]:
            add.append((r, c))
    for a in add:
        if a[0] in s:
            s[a[0]]["count"] += a[1]
        else:
            s[a[0]] = {"count": a[1], "rep": None}

print(sum(v["count"] for v in s.values() if v["count"] > 0))
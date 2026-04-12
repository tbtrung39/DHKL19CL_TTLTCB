pws = input().split(",")
valid = []
for p in pws:
    p = p.strip()
    cond = [6 <= len(p) <= 12,
            any(c.islower() for c in p),
            any(c.isupper() for c in p),
            any(c.isdigit() for c in p),
            any(c in "$#@" for c in p)]
    if all(cond): valid.append(p)
print(",".join(valid))
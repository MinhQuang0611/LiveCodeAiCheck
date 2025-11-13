a = input().strip()
pairs = [a[i:i+2] for i in range(0, len(a), 2)]
seen = set()
result = []
for p in pairs:
    if p not in seen:
        result.append(p)
        seen.add(p)
    else:
        if p == pairs[-1] or pairs.count(p) > 1:  
            result.append(p)
print(" ".join(result))

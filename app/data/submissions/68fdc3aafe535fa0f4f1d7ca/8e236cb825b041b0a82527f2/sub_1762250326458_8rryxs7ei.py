s = input().lstrip("0")
if len(s) <= 3:
    print(s)
else:
    parts = []
    rem = len(s) % 3
    for i in range(rem, len(s), 3):
        parts.append(s[i : i + 3])
    if rem != 0:
        parts.insert(0, s[0:rem])
    print(",".join(parts))

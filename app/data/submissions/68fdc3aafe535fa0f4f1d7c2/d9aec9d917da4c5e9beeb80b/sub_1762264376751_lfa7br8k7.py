a = input().strip()
cp = [a[i:i+2] for i in range(0, len(a), 2)]
c = sorted(set(cp))
b = " ".join(c)
print(b)
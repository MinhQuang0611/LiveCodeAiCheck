a = input().strip()
cap_so = [a[i:i+2] for i in range(0, len(a), 2)]
cap_so2 = sorted(set(cap_so))
print(" ".join(cap_so2))

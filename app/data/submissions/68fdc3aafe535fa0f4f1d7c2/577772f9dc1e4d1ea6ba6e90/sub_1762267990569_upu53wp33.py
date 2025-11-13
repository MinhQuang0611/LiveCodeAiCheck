a = input().strip()
cap = [a[i:i+2] for i in range (0, len(a), 2)]
cap_db = sorted(set(cap), key = lambda x: int(x))
print(' '.join(cap_db))
a = input().strip()
pairs = [a[i:i+2] for i in range(0, len(a), 2)]
unique_pairs = sorted(set(pairs), key=lambda x: int(x))
print(*unique_pairs)

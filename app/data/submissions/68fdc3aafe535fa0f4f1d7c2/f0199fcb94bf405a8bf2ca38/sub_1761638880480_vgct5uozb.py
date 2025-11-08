a = input().strip()

pairs = [a[i:i+2] for i in range(0, len(a), 2)]
print(" ".join(pairs))

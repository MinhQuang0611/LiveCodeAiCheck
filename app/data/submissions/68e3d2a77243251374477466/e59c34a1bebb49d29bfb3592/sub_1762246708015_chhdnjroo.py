s = input().strip()
words = s.split()
n = [w[::-1] for w in words]
print(" ".join(n))
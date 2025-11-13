s = input()
pairs = set()
for i in range(0, len(s) - 1, 2):
    pairs.add(s[i : i + 2])
print(" ".join(sorted(list(pairs))))

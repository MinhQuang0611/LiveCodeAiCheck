s = input().strip()

arr = set()
for i in range(0, len(s), 2):
    arr.add(s[i:i+2])

arr = sorted(arr)
print(" ".join(arr))

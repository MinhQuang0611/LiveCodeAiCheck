def snt(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True
n = int(input())
a = list(map(int, input().split()))
s = sorted([x for x in a if snt(x)])
idx = 0
for i in range(n):
    if snt(a[i]):
        a[i] = s[idx]
        idx += 1
print(*a)

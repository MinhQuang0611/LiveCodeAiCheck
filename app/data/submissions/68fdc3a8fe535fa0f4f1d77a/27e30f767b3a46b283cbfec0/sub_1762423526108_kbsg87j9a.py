def xoay_mang(a, k):
    n = len(a)
    k %= n
    return a[k:] + a[:k]
t = int(input())
for _ in range(t):
    n, k = map(int,input().split())
    a = list(map(int, input().split()))
    ans = xoay_mang(a, k)
    print(*ans)
t = int(input())
for _ in range(t):
    n,k = map(int, input().split())
    a = list(map(int, input().split()))
    k = k % n
    result = a[k:] + a[:k]
    print(" ".join(map(str, result)))
t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    k = k % n        # tránh k > n
    rotated = a[k:] + a[:k]

    print(*rotated)

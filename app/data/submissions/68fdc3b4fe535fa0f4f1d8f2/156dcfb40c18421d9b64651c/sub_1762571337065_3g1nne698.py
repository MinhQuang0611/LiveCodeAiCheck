t = int(input())
for _ in range(t):
    n = int(input())
    count = 0
    k = 1
    while k * (k - 1) // 2 < n:
        if (n - k * (k - 1) // 2) % k == 0:
            count += 1
        k += 1
    print(count - 1)
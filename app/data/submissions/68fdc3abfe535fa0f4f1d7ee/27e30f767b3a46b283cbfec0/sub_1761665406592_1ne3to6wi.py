t = int(input())
for _ in range(t):
    n = int(input())
    sum = 0
    for i in range(2 if n % 2 == 0 else 1, n + 1,2):
        sum += 1/i
    print(f"{sum:.6f}")

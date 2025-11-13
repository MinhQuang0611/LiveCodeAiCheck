t = int(input())
for _ in range(t):
    n = int(input())
    if n % 2 == 0:
        total = sum(1/x for x in range(2, n+1, 2))
    else:
        total = sum(1/x for x in range(1, n+1, 2))
    print(f"{total:.6f}")
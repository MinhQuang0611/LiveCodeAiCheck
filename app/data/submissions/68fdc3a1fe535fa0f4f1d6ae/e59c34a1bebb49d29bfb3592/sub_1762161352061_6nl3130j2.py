t = int(input())
for _ in range(t):
    n = int(input())
    while n % 7 != 0:
        x = int(str(n)[::-1])
        n = n + x
    print(n)
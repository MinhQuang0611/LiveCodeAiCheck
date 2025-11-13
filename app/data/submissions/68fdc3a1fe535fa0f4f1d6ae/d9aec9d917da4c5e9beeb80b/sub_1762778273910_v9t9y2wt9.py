t = int(input())
for i in range(t):
    n = int(input())
    for i in range(1000):
        if n % 7 == 0:
            break
        a = int(str(n)[::-1])
        n = n + a
    print(n)

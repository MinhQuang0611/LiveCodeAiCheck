t = int(input())
for _ in range(t):
    n = int(input())
    pd = n % 10
    n //= 10
    s = pd
    valid = True

    while n > 0:
        d = n % 10
        if abs(d - pd) != 2:
            valid = False
            break
        s += d
        pd = d
        n //= 10

    print("YES" if valid and (s % 10) == 0 else "NO")

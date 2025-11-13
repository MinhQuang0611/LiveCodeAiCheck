t = int(input())
for _ in range(t):
    digits = list(map(int, list(input())))
    n = len(digits)
    rem = 0
    num = 0

    for i in range(n - 1):
        d = digits[-i - 1] + rem
        if d > 4:
            rem = 1
            num = 0
        else:
            rem = 0
            num += d * 10**i

    num += (digits[0] + rem) * (10 ** (n - 1))
    print(num)

t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    res = "1"
    i = 2
    while i * i <= n:
        count = 0
        while n % i == 0:
            count += 1
            n = n // i
        if count > 0:
            res += " * " + str(i) + "^" + str(count)
        i += 1
    if n > 1:
        res += " * " + str(n) + "^1"
    print(res)

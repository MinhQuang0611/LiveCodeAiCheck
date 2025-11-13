n = int(input())
if n <= 1:
    print("false")
else:
    total = 1
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            total += i
            if i != n // i:
                total += n // i
    print("true" if total == n else "false")

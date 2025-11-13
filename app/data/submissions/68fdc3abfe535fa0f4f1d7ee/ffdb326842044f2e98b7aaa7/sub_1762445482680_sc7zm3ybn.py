t = int(input())

while t > 0:
    n = int(input())

    sum = 0

    for i in range(1, n + 1):
        if n % 2 == 0 and i % 2 == 0:
            sum += 1 / i
        elif n % 2 != 0 and i % 2 != 0:
            sum += 1 / i
    print(f"{sum:6f}")

    t -= 1
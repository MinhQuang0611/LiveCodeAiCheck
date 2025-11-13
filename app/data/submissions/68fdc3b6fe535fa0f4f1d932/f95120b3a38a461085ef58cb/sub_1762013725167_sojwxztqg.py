def prime(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True

n, m = map(int, input().split())

for _ in range(n):
    arr = list(map(int, input().split()))
    for num in arr:
        print(1 if prime(num) else 0, end=' ')
    print()  
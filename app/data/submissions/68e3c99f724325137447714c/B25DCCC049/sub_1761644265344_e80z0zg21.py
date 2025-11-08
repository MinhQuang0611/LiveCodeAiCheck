n = int(input())
if n <= 0:
    print("false")
else:
    total = 0
    for i in range(1,n):
        if n % i == 0:
            total += i
    if n == total:
        print("true")
    else:
        print("false")
n = int(input())
total = 0
if n < 1:
    print("false")
else:
    for i in range(1,n):
        if n % i == 0:
            total += i
    if total == n:
        print("true")
    else:
        print("false")
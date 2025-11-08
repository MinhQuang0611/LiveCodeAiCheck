def ktr(n):
    uoc = 0
    for i in range(1, n):
        if n % i == 0:
            uoc += i
    return uoc == n
n = int(input())
if ktr(n):
    print("true")
else:
    print("false")   
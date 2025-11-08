def snt(n):
    if n < 2:
        return False
    for i in range (2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
n, m = map(int, input().split())
for i in range(n):
    row = list(map(int, input().split()))
    kq = []
    for x in row:
        if snt(x):
            kq.append(1)
        else:
            kq.append(0)
    print(*kq)
def nt(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    if n < 2:
        return False
    return True

n = int(input())
a = list(map(int, input().split()))
b = []

for i in a:
    if nt(i) == True:
        b.append(i)
b.sort()
c = iter(b)
kq = []

for i in a:
    if nt(i) == True:
        kq.append(next(c))
    else:
        kq.append(i)

for i in kq:
    print(i, end = ' ')


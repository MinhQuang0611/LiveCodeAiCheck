import math
def sinhhoanvi(a, l, r, res):
    if l == r:
        res.append(''.join(a))
    else:
        for i in range(l, r + 1):
            a[l], a[i] = a[i], a[l]
            sinhhoanvi(a, l + 1, r, res)
            a[l], a[i] = a[i], a[l]
t = int(input())
for j in range(t):
    n = int(input())
    print(math.factorial(n))
    a = [str(i) for i in range(1, n + 1)]
    res = []
    sinhhoanvi(a, 0, n - 1, res)
    res.sort(reverse = True)
    print(' '.join(res))
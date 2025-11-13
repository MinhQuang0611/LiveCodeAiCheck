def hv(a, l, r, res):
    if l == r:
        res.append(''.join(map(str, a)))
    else:
        for i in range(l, r + 1):
            a[l], a[i] = a[i], a[l]
            hv(a, l + 1, r, res)
            a[l], a[i] = a[i], a[l]

t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    a = [i for i in range(1, n + 1)]
    res = []
    hv(a, 0, n - 1, res)
    res.sort(reverse=True)
    print(len(res))
    print(' '.join(res))

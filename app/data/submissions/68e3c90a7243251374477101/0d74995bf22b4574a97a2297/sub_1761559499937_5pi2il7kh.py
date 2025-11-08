def tich(n):
    s = str(n)
    if len(s) < 2:
        return 0
    mx = 0
    for i in range(len(s) - 1):
        so1 = int(s[i])
        so2 = int(s[i+1])
        d = so1 * so2
        if d > mx:
            mx = d
    return mx
n = int(input())
print(tich(n))


n = int(input())
t = list(map(int,input().split()))
if n != len(t):
    print()
else:
    a=max(t)
    b=min(t)
    if a == b:
        t.remove(a)
    else:
        t.remove(a)
        t.remove(b)
    m = sum(t)
    p=float(m/len(t))
    print(p)
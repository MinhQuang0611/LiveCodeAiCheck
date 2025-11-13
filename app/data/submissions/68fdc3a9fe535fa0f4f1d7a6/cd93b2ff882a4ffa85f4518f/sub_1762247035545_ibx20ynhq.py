t=int(input())
for _ in range(t):
    s=input().strip()
    s2=""
    for ch in s:
        if ch in "0123456789":
            s2=s2+ch 
        else:
            s2=s2+" "
    s2=s2.split()
    k=10**30
    for x in s2:
        n=int(x)
        if n<k:
            k=n
    print(k)

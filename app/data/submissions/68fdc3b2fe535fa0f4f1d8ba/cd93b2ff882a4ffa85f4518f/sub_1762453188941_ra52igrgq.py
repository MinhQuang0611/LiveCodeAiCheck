def chia(n):
    check=False
    k=0
    while(n>0):
        k=k+n%10
        n=n//10
    if k%10==0:
        check=True
    return check
def hieu(s: str):
    check=True
    for i in range (0,len(s)-1):
        k1=int(s[i])
        k2=int(s[i+1])
        if abs(k1-k2)!=2:
            check=False
            break
    return check
t=int(input())
for _ in range (t):
    n=int(input())
    s=str(n)
    if hieu(s) and chia(n):
        print("YES")
    else:
        print("NO")
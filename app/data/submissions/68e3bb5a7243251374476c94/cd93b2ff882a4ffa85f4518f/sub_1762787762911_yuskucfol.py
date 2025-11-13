def check(num,k):
    a=[]
    for c in num:
        while a and k>0 and a[-1]>c:
            a.pop()
            k-=1
        a.append(c)
    while k>0:
        a.pop()
        k-=1
    res=''.join(a).lstrip('0')
    return res if res else '0'
n=input().split()
k=int(n[1])
num=n[0]
print(check(num,k)) 

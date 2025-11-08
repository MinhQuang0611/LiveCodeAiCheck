t=int(input())
while t:
    t-=1
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    ln=max(a)
    if k>=ln:
        a.append(k)
    else:
        a.insert(len(a)-1,k)
    am=[]
    duong=[]
    for i in a:
        if i<0:
            am.append(i)
        else:
            duong.append(i)
    A=am+duong
    for i in A:
        print(i,end=" ")


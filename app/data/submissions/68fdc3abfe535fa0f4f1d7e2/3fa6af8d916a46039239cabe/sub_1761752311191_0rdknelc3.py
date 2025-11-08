def giaithua(n):
    tich=1
    for i in range(2,n+1):
        tich*=i
    return tich
t=int(input())
while t:
    t-=1
    s=input()
    tong=0
    for i in s:
        tong+=giaithua(int(i))
    if tong==int(s):
        print("Yes")
    elif s=="0":
        print("Yes")
    else:
        print("No")
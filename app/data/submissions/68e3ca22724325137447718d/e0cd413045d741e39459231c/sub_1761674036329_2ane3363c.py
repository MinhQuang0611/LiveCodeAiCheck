n=int(input())
b=0
for i in range(1,n+1):
    a=i
    tong=0
    while a>0:
        du=a%10
        tong+=du
        a//=10
    if tong%5==0 and '7' in str(i):
        b+=1
print(b)

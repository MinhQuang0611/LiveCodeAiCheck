tong=0
a=int(input())
while a!=0:
    tong+=a%10
    a//=10
    if a==0 and tong>10:
        a=tong
        tong=0
print(tong)
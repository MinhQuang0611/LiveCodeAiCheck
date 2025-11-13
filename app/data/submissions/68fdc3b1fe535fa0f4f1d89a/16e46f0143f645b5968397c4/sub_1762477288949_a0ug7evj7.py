tong=0
a=int(input())
count=1
while a!=0:
    tong+=a%10
    a//=10
    if a==0 and tong>10:
        count+=1
        a=tong
        tong=0
print(count)
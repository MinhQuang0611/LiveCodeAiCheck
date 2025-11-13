a=int(input())
if a<0:
    a*=-1
tong=0
while a!=0:
    tong+=a%10
    a//=10
print(tong)
    
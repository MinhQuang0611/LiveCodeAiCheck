n=int(input())
m=abs(n)
tong=0
while m>0:
    so_cuoi=m%10
    tong=tong+so_cuoi
    m//=10
print(tong)
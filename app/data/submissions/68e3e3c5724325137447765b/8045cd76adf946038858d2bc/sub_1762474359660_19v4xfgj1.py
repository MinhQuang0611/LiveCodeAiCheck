s=int(input())
n=abs(s)
tong=0
while n>0:
    so=n%10
    tong += so
    n=n//10
print(tong)


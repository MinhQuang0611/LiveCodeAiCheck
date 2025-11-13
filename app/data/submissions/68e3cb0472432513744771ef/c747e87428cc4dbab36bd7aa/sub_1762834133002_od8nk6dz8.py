n=int(input())
while n >= 10:
    tong=0
    while n>0:
        tong+=n%10
        n=n//10
    n=tong
print(n)
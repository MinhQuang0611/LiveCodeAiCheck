n=int(input())
if n==-1:
    print(-1)
elif n < 10:
    print(n)
else:
    while n >= 10:
        tong = 0
        for i in str(n):
            tong += int(i)
        n = tong 
    print(n)
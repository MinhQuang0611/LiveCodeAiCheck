n = int(input())
a=0
while n >= 10 :
    tong = 0
    while n > 0:
        tong += n % 10
        n //= 10
    n = tong 
    a += 1
print(a)
def test(n):
    tmp = 0
    tonggt = 1
    tong = 0
    x = n
    while n > 0:
        tmp = n % 10
        for i in range(1, tmp + 1):
            tonggt *= i
        tong += tonggt
        n //= 10
        tmp = 0
        tonggt = 1
    
    if tong == x:
        print('Yes')
    else: 
        print('No')
    

a = list(map(int, input().split()))

for i in range(len(a)):
    test(a[i])
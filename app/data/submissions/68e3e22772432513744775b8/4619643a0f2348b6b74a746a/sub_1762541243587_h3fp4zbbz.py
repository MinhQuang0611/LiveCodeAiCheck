n = int(input())
if n == 0:
    a = 1
    print(a)
elif n >= 1:
    tich = 1
    for i in range(1,n+1):
        tich *= i
    print(tich)
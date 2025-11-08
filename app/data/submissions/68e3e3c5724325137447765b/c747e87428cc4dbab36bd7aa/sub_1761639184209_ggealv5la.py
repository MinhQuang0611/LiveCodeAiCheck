n=int(input())
tong=0
if n<0:
    n=-n
    while n!=0:
        di=n%10
        tong=tong+di
        n=n//10
    print(tong)
else:
    while n!=0:
        di=n%10
        tong=tong+di
        n=n//10
    print(tong)


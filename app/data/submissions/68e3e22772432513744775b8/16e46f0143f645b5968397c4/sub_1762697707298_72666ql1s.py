n=int(input())
tich=1
if n>0:
    for i in range(1,n+1):
        tich*=i
    print(tich)
if n==0:
    print("1")
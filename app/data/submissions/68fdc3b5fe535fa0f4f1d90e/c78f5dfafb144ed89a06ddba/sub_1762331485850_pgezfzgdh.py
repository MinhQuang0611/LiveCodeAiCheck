n = int(input())
while n>0:
    n-=1
    tong=0
    tich=1
    t=list(map(int,input()))
    for i in range(len(t)):
        if (i+1) % 2 == 1:
            tich*=int(t[i])
        else:
            tong+=int(t[i])
    print(tich, tong)
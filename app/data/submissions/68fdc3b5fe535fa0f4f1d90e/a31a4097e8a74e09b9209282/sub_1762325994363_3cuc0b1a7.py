import math
dem=1
T=int(input())
while(T):
    T-=1
    n=input()
    nh=1
    co=0
    for i in range(len(n)):
        if i%2==0: nh*=int(n[i])
        else: co+=int(n[i])
    print(f"{nh} {co}")
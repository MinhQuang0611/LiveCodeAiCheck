import math
dem=1
T=int(input())
while(T):
    T-=1
    s=input()
    s+=" "
    for i in range(len(s)):
        if s[i]==s[i+1]: dem+=1
        else:
            print(f"{dem}{s[i]}",end="")
            dem=1
            if s[i+1]==" ": break
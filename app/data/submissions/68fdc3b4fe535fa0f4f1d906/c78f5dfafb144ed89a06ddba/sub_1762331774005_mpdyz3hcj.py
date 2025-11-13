n = int(input())
while n>0:
    n-=1
    a=input()
    if (a[0] == a[-1]) == True:
        print("YES")
    else:
        print("NO")
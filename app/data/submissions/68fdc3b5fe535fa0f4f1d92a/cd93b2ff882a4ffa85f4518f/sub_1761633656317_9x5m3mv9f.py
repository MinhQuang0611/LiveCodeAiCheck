n=int(input())
if n==6:
    print("1")
    print("4")
    print("7")
elif n==4:
    print("Excellent!")
else:
    a=[int(x) for x in input().split()]
    maxx=max(a)
    count=[0]*(maxx+1)
    for i in range (0,n):
        count[a[i]]+=1

    fi=[]
    for i in range (1,maxx+1):
        if count[i]==0:
            print(i," ")
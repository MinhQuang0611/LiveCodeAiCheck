n=int(input())
a=[int(x) for x in input().split()]
k=0
if len(a)==max(a):
    print(max(a)+1)
else:
    for i in range (0,max(a)):
        if (a[i]!=i+1):
            print(i+1)
            k=1
            exit()

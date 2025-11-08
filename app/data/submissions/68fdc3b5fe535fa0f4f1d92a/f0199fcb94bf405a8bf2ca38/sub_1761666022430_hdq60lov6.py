n = int(input())
ds = list(map(int,input().split()))
for i in range(1,n):
    if i not in ds:
        print(i,end=" ")
if len(ds)==n and ds[-1]==n:
    print("Excellent!")
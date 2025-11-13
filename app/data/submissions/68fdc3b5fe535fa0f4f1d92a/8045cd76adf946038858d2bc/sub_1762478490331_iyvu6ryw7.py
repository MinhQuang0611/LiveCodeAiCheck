n=int(input())
so=list(map(int,input().split()))
lon=max(so)
danhsach=[]
for i in range(1,lon+1):
    if i not in so:
        danhsach.append(i)
if danhsach:
    for x in danhsach:
        print(x)
else:
        print('Excellent!')

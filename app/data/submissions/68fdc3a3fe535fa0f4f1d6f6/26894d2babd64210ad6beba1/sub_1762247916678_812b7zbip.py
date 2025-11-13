a, k ,n = map(int,input().split())
x = []
for i in range(a, n+1):
    if i % k == 0:
        x.append(i-a)
if(len(x)==0):
    print(-1)
else:
    print(*sorted(x))
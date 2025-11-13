a=[int(x) for x in input().split()]
minn=10**9
profit=0
mapro=0
for i in a:
    pri=i
    if pri<minn:
        minn=pri 
    profit=pri-minn
    if profit>mapro:
        mapro=profit
print(mapro)

    
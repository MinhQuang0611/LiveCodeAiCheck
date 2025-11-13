n=int(input())
r=list(map(float,input().split()))
gtln=max(r)
gtnn=min(r)
new =[x for x in r if x!=gtln and x !=gtnn]
if len(new)==0:
    print("Not enough value")
else:
    tb=sum(new)/len(new)
    if tb.is_integer():
        print(int(tb))
    else:
        print(f"{tb:.2f}")

n=int(input())
so=list(map(int, input().split()))
lon=max(so)
be=min(so)
somoi=[]
for x in so:
    if x != lon and x != be:
        somoi.append(x)
tbc= sum(somoi)//len(somoi)
print(tbc)

n=int(input())
a=list(map(float, input().split()))
maxi=max(a)
mini=min(a)
lists=[x for x in a if x!=maxi and x!=mini]
tb=sum(lists)/len(lists)
print(int(tb))
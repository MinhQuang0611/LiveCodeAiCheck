ds=list(map(int,input().split()))
if len(ds)>0:  
   print(sum(ds)/len(ds))
else:
    print(f"{0:.1f}")
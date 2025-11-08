ds = list(map(float, input().split()))
if ds==[]:
    print(0.0)
else: 
    tb = sum(ds) / len(ds)
    print(tb)
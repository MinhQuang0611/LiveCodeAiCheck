n=int(input())
ds=[]
for i in range(n):
    kt=input()
    if kt not in ds:
        if kt!=-1:
            ds+=[kt]
print(len(ds))
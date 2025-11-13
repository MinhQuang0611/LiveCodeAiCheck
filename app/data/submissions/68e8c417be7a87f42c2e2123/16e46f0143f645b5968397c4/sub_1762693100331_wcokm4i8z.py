max=-999
a=list(map(int,input().split()))
for i in a:
    if i>max:
        max=i
print(max)
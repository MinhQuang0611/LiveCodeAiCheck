n=int(input())
chan=0
le=0
for i in str(n):
    if int(i) % 2 == 0:
        chan+=1
    else:
        le+=1
l=[chan, le]
print(l)
l=list(map(int, input().split()))
start=l[0]
end=l[1]
chan=0
le=0
for i in range(start, end+1):
    if i % 2 == 0:
        chan+=1
    else:
        le+=1
b=[chan, le]
print(*b)

n=list(map(int,input().split()))
falses=[]
for i in range(1, len(n)+1):
    if (i in n)==False:
        falses.append(str(i))
print(" ".join(falses))
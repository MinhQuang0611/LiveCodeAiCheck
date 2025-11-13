a,b=map(int,input().split())
tongchan=0
tongle=0
for i in range(a,b+1):
    k=str(i)
    for j in k:
        h=int(j)
        if h%2==0:
           tongchan+=1
        else:
           tongle+=1
print(tongchan,tongle)
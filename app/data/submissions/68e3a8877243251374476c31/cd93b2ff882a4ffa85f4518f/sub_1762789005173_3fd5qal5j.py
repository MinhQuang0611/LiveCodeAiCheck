s=input()
s1=s[1:-1].replace(","," ")
s1=s1.split()
a=[0]*1000001
luu=[]
maxx=0
for ch in s1:
    k=int(ch)
    maxx=max(maxx,k)
    a[k]+=1
s3=''
for i in range (0,maxx):
    if a[i]==2:
        luu.append(i)
print('[' + ','.join(map(str, luu)) + ']')
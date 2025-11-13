s=input()
s1=""
l=0
a=[0]*101
for ch in s:
    s1=s1+ch 
    l=l+1
    if l==2:
        k=int(s1)
        a[k]+=1
        s1=""
        l=0
for i in range (9,101):
    if a[i]>=1:
        print(i,end=" ")
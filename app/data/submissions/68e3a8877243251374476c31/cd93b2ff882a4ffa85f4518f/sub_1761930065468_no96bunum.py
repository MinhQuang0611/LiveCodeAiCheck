s=input()
s1=""
z=0
for ch in s:
    if ch in ('01234567890-'):
        s1=s1+ch 
    elif ch==",":
        s1=s1+" "
        z=z+1
s1=s1.split()
a=[0]*len(s)
check=[0]*1000000
for i in range (0,len(s1)):
        k=int(s1[i])
        a.append(k)
for i in range (0,len(a)):
    if a[i]>0:
        check[a[i]]+=1
kq=[]
for i in range (1,max(a)+1):
    if check[i]==2:
        kq.append(i)
kq2='['
for i in range (0,len(kq)):
    if i==len(kq)-1:
        kq2=kq2+str(kq[i])
    else:
        kq2=kq2+str(kq[i])+","
print(kq2,end="]")
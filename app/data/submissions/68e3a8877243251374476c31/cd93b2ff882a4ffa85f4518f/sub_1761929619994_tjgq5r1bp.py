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
for ch in s1:
        k=int(ch)
        a.append(k)
#for i in range (0,len(a)):
   # if a[i]>0:
        
print(a)

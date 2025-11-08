s=input()
s1=""
for ch in s:
    if ch in "-1234567890":
        s1=s1+ch
    if ch == ",":
        s1=s1+" "
s1=s1.split()
s2=""
for i in range (0,len(s1)):
    k=int(s1[i])
    if i==len(s1)-1:
        s2=s2+str(k*k)
    else:
        s2=s2+str(k*k)+","
print("[",s2,']',sep="")
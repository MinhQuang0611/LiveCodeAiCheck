s=input()
l=0
s2=""
for ch in s:
    s2=s2+ch 
    l=l+1
    if l==2:
        s2=s2+" "
        l=0
s2=s2.split()
s2=dict.fromkeys(s2)
print(*s2)
s=input()
s1=""
l=0
for ch in s:
    s1=s1+ch 
    l=l+1
    if l==2:
        print(s1," ",sep="",end="")
        s1=""
        l=0
    
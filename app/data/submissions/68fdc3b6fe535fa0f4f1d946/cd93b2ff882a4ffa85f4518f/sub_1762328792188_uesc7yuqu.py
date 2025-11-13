s=input()
s=s.lower()
s=s.title()
s2=""
for i in range (0,len(s)):
    if s[i] in "1234567890qwertyuiopasdfghjklzxcvbnmQERTYUIOPASDFGHJKLZXCVBNMwW:,":
        s2=s2+s[i]
    elif s[i]==" ":
        s2=s2+" "
s2=s2.split()
for ch in s2:
    print(ch,end=" ")
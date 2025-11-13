s=input()
s=s.lower()
s=s.title()
s2=""
for ch in s:
    if ch in "1234567890qwertyuiopasdfghjklzxcvbnmQƯERTYUIOPASDFGHJKLZXCVBNM:,":
        s2=s2+ch
    elif ch==" ":
        s2=s2+" "
print(s2)
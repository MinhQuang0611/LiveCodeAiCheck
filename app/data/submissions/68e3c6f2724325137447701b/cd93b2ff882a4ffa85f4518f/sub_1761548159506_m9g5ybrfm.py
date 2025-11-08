k=0
s=str(input())
for i in range (0,len(s)):
    if s[i].isdigit():
        k=1
        break
if k==1:
    print("false")
else:
    print("true")
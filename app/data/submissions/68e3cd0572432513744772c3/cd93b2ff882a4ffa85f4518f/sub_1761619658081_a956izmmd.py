s=str(input())
k=0
for i in range(0,len(s)):
    if s[i] == s[i+1]:
        k=1
        break
if k==1:
    print("true")
else:
    print("false")
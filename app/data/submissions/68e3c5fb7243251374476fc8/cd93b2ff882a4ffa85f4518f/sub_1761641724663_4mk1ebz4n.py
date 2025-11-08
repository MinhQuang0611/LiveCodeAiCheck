s=input()
t=input()
if len(s) > len(t):
    print("false")
    exit()
for i in range (0,len(s)):
    if s[i]!=t[i]:
        print("false")
        exit()
print("true")
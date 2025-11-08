def check(s):
    if s[0]!="6":
        return 0
    for i in s:
        if i!="6" and i!="8":
            return 0
    for i in range(1,len(s)-1):
        if s[i]=="8" and (s[i]==s[i-1]==s[i+1]):
            return 0
    return 1
if check(input()):
    print("YES")
else:
    print("NO")
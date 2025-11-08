def check(s):
    if s=="2244":
        return 0
    for i in range(len(s)-1):
        if int(s[i])>int(s[i+1]):
            return 0
    return 1
t=int(input())
while t:
    s=input()
    if check(s):
        print("YES")
    else:
        print("NO")
    t-=1
t = int(input())
for i in range(t):
    s = str(input())
    if s[0] == s[-1]:
        print("YES")
    else:
        print("NO")
t = int(input())
for i in range(t):
    s = input().strip()
    if s[0] == s[-1]:
        print("YES")
    else:
        print("NO")
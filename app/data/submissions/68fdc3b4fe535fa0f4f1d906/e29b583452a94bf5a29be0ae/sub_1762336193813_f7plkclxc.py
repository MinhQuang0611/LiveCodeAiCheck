t = int(input())
for _ in range(t):
    s = input()
    if len(s) > 0 and s[0] == s[-1]:
        print("YES")
    else:
        print("NO")

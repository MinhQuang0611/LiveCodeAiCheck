t=int(input())
for _ in range(t):
    s = input().strip()
    if s[0]==s[-1]:
        print("YES")
    else:
        print("NO")
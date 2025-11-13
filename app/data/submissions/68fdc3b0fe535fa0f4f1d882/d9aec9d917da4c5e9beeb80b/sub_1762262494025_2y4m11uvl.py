t = int(input())
for i in range(t):
    s = input().strip()
    if len(s) >= 2 and s[-2:] == "86":
        print("YES")
    else:
        print("NO")

n = int(input())
for _ in range(n):
    t = input().strip()
    if t[0] == t[-1]:
        print("YES")
    else:
        print("NO")
def solve():
    s = input().strip()
    start = s[0]
    end = s[-1]
    if start == end:
        print("YES")
    else:
        print("NO")
t = int(input())
for _ in range(t):
    solve()
import sys
input = sys.stdin.readline
def solve():
    s = input().strip()
    res = []
    a = s[0]
    cnt = 0
    for char in s:
        if char == a:
            cnt += 1
        else:
            res.append(str(cnt))
            res.append(a)
            a = char
            cnt = 1
    res.append(str(cnt))
    res.append(a)
    print("".join(res))
t = int(input())
for _ in range(t):
    solve()
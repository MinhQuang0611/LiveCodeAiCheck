n = int(input())
for _ in range(n):
    t = input().strip()
    if not all(ch in "47" for ch in t):
        print("NO")
    else:
        print("YES")
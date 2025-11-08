t = int(input())
for _ in range(t):
    s = input().strip()
    print("YES" if all(c in "47" for c in s) else "NO")

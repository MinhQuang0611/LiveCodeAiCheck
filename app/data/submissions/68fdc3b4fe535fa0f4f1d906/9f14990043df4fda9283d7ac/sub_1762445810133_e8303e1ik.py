t = int(input())
for _ in range(t):
    s = input().strip()  # đọc 1 chuỗi
    if s[0] == s[-1]:
        print("YES")
    else:
        print("NO")
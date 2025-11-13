t = int(input())
result = []
for i in range (t):
    s = input().strip()
    is_magic = True
    n = len(s)
    if n >= 3:
        for i in range(2, n):
            if s[i] != s[i - 2]:
                is_magic = False
                break
    if is_magic:
        result.append("YES")
    else:
        result.append("NO")
print("\n".join(result))
   
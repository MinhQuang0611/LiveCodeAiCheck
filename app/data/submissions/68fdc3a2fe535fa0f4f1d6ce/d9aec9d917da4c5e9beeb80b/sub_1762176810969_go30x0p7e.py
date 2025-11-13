t = int(input())
for q in range(t):
    n = int(input())
    s = str(n)
    if s == s[::-1]:
        print("NO")
    elif sum(int(d) for d in s) > 10:
        print("YES")
    else:
        print("NO")

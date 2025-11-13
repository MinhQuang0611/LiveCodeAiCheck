t = int(input())
for _ in range(t):
    s = input()
    c = s[0]
    for i in range(1, len(s)):
        if s[i] > c:
            c = s[i]
        elif s[i] < c:
            print("NO")
            break
    else:
        print("YES")

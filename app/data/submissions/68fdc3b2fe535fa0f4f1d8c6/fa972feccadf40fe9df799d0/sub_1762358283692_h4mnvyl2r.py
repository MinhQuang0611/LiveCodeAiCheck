t = int(input())
for _ in range(t):
    s = input()
    a = True
    for i in range(len(s)-1):
        if s[i] > s[i + 1]:
            a = False
            break
    if a:
        print("YES")
    else:
        print("NO")
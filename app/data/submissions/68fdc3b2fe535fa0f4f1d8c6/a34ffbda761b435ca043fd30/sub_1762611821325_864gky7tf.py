t = int(input())
for i in range(t):
    n = input()
    a = False
    for i in range(1, len(n)):
        if n[i-1]<=n[i]:
            a = True
    if a:
        print("YES")
    else:
        print("NO")
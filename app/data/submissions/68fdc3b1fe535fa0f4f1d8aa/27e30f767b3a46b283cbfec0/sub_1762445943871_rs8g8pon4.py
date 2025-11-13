t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    check = False
    for i in range(n):
        if a[i] > b[i]:
            check = True
    if check:
        print("NO")
    else:
        print("YES")

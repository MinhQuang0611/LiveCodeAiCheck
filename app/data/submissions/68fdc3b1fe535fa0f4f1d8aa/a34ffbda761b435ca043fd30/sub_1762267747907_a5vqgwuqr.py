t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()
    b.sort()
    valid = True
    for i in range(n):
        if a[i]>b[i]:
            valid = False
            break
    if valid:
        print('YES')
    else:
        print("NO")
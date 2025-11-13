a = int(input())
for i in range(a):
    b = int(input())
    m = list(map(int, input().split()))
    n = list(map(int, input().split()))
    m.sort()
    n.sort()
    dung=True
    for i in range(b):
        if m[i]>n[i]:
            dung=False
    if dung:
        print('YES')
    else:
        print('NO')
t = int(input())
for _ in range(t):
    n = int(input())
    a = list( input().split())
    cnt1, cnt2 = 1,0
    a.sort()
    for i in range(1, n):
        if a[i] == a[i-1]:
            cnt1 += 1
        elif a[i] != a[i-1]:
            if cnt1 > n / 2:
                print(a[i-1])
                cnt2 += 1
            cnt1 = 1
    if  cnt1 > n / 2:
        print(a[i])
        cnt2 += 1
    if cnt2 == 0:
        print('NO')


n = int(input())
a = list(map(float, input().split()))

mn = min(a)
mx = max(a)

if mn == mx:
    print(mn)
else:
    s = 0
    cnt = 0
    for x in a:
        if x != mn and x != mx:
            s += x
            cnt += 1
    print(int(s / cnt))

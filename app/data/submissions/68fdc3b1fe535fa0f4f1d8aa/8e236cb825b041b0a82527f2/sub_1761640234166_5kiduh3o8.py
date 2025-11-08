t = int(input())
for _ in range(t):
    n = int(input())
    ta = list(map(int, input().split()))[:n]
    tb = list(map(int, input().split()))[:n]

    ta.sort()
    tb.sort()

    for i in range(n):
        if ta[i] > tb[i]:
            print("NO")
            break
    else:
        print("YES")
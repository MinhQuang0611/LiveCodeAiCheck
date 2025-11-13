t = int(input())
for _ in range(t):
    n = int(input())
    k = []
    for i in range(n):
        a, b = map(int, input().split())
        k.append([a, b])
    k.sort( key = lambda x : x[0])
    cnt = 1
    c = [k[0]]
    for i in range(1,len(k)):
        if k[i][0] >= c[-1][1]:
            cnt += 1
            c.append(k[i])
        else:
            if i < len(k):
                if  k[i+1][1] <= c[-1][1]:
                    c.append(k[i])
                   
    print(cnt)



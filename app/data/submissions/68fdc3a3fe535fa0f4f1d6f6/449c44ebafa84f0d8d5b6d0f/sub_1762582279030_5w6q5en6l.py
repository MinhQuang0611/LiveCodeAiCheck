a,k,n = map(int, input().split())
for i in range(a, n + 1):
    cnt = 0
    if i % k == 0:
        cnt += 1
        print( i - a, end = ' ')
if cnt == 0:
    print('-1')
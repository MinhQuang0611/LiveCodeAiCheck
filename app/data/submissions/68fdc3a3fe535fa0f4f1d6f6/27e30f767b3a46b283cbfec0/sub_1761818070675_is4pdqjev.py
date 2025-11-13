a, k, n = map(int, input().split())
check = False
for x in range(a,n+1):
    if x % k == 0:
        print(x-a,end = ' ')
        check = True
if not check:
    print(-1)

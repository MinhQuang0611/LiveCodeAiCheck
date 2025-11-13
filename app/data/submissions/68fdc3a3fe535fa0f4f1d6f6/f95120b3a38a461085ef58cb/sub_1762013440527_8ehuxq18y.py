a,k,b = map(int,input().split())
start = (a // k + 1) * k
if start > b:
    print(-1)
else:
    res = [str(x-a)for x in range(start,b+1,k)]
    print(" ".join(res))
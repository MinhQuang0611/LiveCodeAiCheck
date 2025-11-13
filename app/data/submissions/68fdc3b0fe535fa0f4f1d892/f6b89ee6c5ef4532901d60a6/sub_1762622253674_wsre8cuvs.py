t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int, input().split()))
    dem=[]
    for d in set(a):
        dem.append((d, a.count(d)))
    for key, value in dem:
        if value % 2 ==1:
            print(key)







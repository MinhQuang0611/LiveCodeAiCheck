n = list(map(float, input().split()))
if len(n) != 0:
    avg = sum(n)/len(n)
    print(avg)
else:
    print(0.0)
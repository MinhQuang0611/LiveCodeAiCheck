n = input().split()
if not n:
    print(0.0)
else:
    n = list(map(float, n))
    avergae = sum(n)/len(n)
    print(avergae)
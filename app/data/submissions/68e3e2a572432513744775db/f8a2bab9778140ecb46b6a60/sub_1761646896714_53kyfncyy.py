a = list(map(int, input().split()))
if len(a) > 0:
    b = sum(a)/len(a)
    print(float(b))
else:
    print('0.0')
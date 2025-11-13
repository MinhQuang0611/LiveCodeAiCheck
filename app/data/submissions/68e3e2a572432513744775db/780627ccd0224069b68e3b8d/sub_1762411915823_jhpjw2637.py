a = list(map(int, input().split()))
if len(a) == 0:
    print('0.0')
else:
    print(f"{sum(a)/len(a):.15f}")
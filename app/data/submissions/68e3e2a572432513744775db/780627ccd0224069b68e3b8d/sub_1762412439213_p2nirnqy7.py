a = list(map(int, input().split()))
if len(a) == 0:
    print('0.0')
else:
    print("{:.15f}".format(sum(a)/len(a)))
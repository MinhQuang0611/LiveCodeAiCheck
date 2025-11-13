import math
n = int(input())
for _ in range(n):
    m  = int(input())
    tong = sum(math.factorial(int(i)) for i in str(m))
    if m == 0:
        print('Yes')
    elif tong ==m:
        print('Yes')
    else:
        print('No')        
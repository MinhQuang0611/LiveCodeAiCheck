t = int(input())
for i in range(t):
    n, x, m = map(int, input().split())
    import math
    a = math.log(m/n , 1 + x/100)
    print(int(a)+1)
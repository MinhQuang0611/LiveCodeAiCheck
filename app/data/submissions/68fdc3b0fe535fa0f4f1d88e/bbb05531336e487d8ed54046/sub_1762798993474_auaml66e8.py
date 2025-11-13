import math  # dùng để tính gcd

n = int(input())
a = list(map(int, input().split()))

for i in range(n - 1):
    for j in range(i + 1, n):
        if math.gcd(a[i], a[j]) == 1: 
            print(a[i], a[j])

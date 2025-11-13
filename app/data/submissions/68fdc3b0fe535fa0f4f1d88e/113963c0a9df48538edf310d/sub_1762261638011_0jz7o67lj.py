from math import gcd
n = int(input())
arr = [int(i) for i in input().split()]

for i in range(n):
    for j in range(i+1, n):
        if gcd(arr[i], arr[j]) == 1:
            print(arr[i], arr[j])


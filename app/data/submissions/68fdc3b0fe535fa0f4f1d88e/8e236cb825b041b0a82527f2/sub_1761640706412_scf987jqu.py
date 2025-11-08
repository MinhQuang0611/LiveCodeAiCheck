def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


n = int(input())
arr = list(map(int, input().split()))
arr.sort()

for i in range(0, n-1):
    for j in range(i+1, n):
        if gcd(arr[i], arr[j]) == 1:
            print(arr[i], arr[j])

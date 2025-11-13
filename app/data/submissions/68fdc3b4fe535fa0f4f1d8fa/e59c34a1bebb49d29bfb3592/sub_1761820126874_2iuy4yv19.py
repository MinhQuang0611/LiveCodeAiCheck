def prime(x):
    if x < 2:
        return False
    for i in range(2,int(x**0.5)+1):
        if x % i == 0:
            return False
    return True
n = int(input())
arr = list(map(int,input().split()))   
primes = sorted([x for x in arr if prime(x)])
j = 0
for i in range(n):
    if prime(arr[i]):
        arr[i] = primes[j]
        j += 1
print(*arr)
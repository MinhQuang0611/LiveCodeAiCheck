import math
n = int(input())
arr = list(map(int,input().split()))
for i in range(n):
    for j in range(i+1,n):
        if math.gcd(arr[i],arr[j]) == 1:
            print(arr[i],arr[j])    

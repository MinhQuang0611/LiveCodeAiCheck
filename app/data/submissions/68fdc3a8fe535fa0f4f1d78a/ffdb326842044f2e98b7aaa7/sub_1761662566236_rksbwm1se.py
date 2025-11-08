from math import gcd


n, k = map(int, input().split())

result = []
for i in range(10**(k-1), 10**k):
    if gcd(n, i) == 1:
        result.append(i)

# In ra kết quả
for j in range(0, len(result), 10):
    print(" ".join(map(str, result[j:j+10])))
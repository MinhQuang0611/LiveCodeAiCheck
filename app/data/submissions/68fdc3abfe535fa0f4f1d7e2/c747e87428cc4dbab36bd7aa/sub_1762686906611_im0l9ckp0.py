import math
t = int(input())
numbers=[]
for _ in range(t):
    numbers.append(int(input()))
for n in numbers:
    if n==0:
        print('Yes')  
        continue
    digits=[]
    for ch in str(n):
        digits.append(int(ch))
    factorial_sum = 0
    for d in digits:
        factorial_sum += math.factorial(d)
    if factorial_sum == n:
        print('Yes')
    else:
        print('No')

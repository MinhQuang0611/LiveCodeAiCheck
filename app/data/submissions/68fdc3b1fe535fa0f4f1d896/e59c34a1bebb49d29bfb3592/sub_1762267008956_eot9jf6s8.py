import math
def prime(x):
    if x < 2:
        return False
    for i in range(2,int(x**0.5)+1):
        if x % i == 0:
            return False
    return True
def euler(n):
    lst =[]
    for i in range(1,n+1):
        if math.gcd(n,i) == 1:
            lst.append(i)
    return len(lst)
t = int(input())
for _ in range(t):
    n = int(input())
    ans = euler(n)
    if prime(ans):
        print("YES")
    else:
        print("NO")

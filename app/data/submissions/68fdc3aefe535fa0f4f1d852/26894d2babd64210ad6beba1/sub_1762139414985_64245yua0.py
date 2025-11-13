import math

def snt(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if(n % i == 0):
            return False
    return True

t = int(input())

while(t> 0):
    t-=1
    a, b = map(int, input().split())
    c = math.gcd(a, b)
    sum = 0
    c = str(c)
    #print(c)
    for i in c:
        sum += int(i)
    #print(sum)
    if snt(sum):
        print("YES")
    else:
        print("NO")

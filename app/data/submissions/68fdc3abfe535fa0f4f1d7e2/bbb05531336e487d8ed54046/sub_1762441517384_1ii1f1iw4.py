def gt(x):
    res = 1
    for i in range(1, x + 1):
        res *= i
    return res

for _ in range(int(input())):
    n = int(input())
    if n == 0:  
        print("Yes")
        continue
    s = 0
    for d in str(n):
        s += gt(int(d))
    print("Yes" if s == n else "No")


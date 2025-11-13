def tong(n):
    sum = 1
    for i in range(1, n + 1):
        sum *= i
    return sum

t = int(input())

while t > 0:
    t -= 1
    n = input()
    sum = 0
    for i in n:
        sum += tong(int(i))
    if sum == int(n):
        print("YES")
    else:
        print("NO")
    

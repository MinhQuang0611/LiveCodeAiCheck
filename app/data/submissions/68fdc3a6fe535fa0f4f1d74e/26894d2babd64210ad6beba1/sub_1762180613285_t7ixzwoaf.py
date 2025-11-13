t = int(input())

while t > 0:
    t -= 1
    a = list(map(int, input().split()))
    a.sort()
    sum = 0
    for i in range(len(a)):
        sum += a[i]
        if i == 2:
            break
    print(sum)
def dem(n):
    sum = 0
    for i in range(1,n):
        a = 0
        b = i
        while a < n:
            a +=b
            b += 1
            if a ==n:
                sum +=1
                break
    return sum
c = int(input())
for _ in range(c):
    d = int(input())
    print(dem(d))

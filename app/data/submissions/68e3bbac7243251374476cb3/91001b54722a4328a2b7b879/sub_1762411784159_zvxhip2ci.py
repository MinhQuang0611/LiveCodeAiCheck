a, b = map(int, input().split())
while b > 0:
    a += 1
    b -= 1
while b < 0:
    a -= 1
    b +=1
print(a)
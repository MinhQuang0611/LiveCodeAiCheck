t = int(input())

print(t, end = " ")
while t != 1:
    if t % 2 == 0:
        t //= 2
    else:
        t = t * 3 + 1
    print(t, end = " ")
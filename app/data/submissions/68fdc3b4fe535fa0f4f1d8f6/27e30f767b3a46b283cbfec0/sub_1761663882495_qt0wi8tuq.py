a1,a2,a3,a4 = map(int, input().split())
count = -1
while not (a1 == 0 and a2 == 0 and a3 == 0 and a4 == 0):
    b1 = abs(a1-a2)
    b2 = abs(a2-a3)
    b3 = abs(a3-a4)
    b4 = abs(a4-a1)
    a1,a2,a3,a4 = b1,b2,b3,b4
    count += 1
print(count)

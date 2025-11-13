a1, a2, a3, a4 = map(int, input().split())

i = 0
while not (a1 == a2 == a3 == a4):
    prev_a1 = a1
    a1 = abs(a1 - a2)
    a2 = abs(a2 - a3)
    a3 = abs(a3 - a4)
    a4 = abs(a4 - prev_a1)
    i += 1
print(i)
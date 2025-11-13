count = 0
a1, a2, a3, a4 = list(map(int, input().split()))

while not (a1 == a2 and a2 == a3 and a3 == a4):
    count += 1
    old_a1 = a1
    a1 = abs(a1 - a2)
    a2 = abs(a2 - a3)
    a3 = abs(a3 - a4)
    a4 = abs(a4 - old_a1)
print(count)
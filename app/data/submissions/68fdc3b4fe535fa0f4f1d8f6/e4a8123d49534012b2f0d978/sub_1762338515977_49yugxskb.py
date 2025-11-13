
a1, a2, a3, a4 = map(int, input().split())
   
count = 0
while not (a1 == a2 == a3 == a4):
        na1 = abs(a1 - a2)
        na2 = abs(a2 - a3)
        na3 = abs(a3 - a4)
        na4 = abs(a4 - a1)
        a1, a2, a3, a4 = na1, na2, na3, na4
        count += 1
print(count)
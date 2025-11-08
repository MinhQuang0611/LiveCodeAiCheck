n = int(input())
for i in range(n):
    s = input()
    a = []
    dem = 0
    for x in s:
        if x == '(':
            dem += 1
            a.append(dem)
            print(dem, end=" ")
        else:
            print(a.pop(), end=" ")
    print()
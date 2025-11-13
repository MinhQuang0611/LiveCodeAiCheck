n = int(input())
a = list(map(int, input().split()))
v = max(a)
check = True
for i in range(1, v + 1):
    if a.count(i) == 0:
        print(i)
        check = False
if check == True:
    print('Excellent!')




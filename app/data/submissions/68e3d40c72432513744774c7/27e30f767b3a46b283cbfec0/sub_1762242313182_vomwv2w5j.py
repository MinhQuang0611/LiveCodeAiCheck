num_1 = int(input())
ar_1 = list(map(int, input().split()))
num_2 = int(input())
ar_2 = list(map(int, input().split()))
lst = []
check = False
for i in ar_2:
    if i in ar_1:
        lst.append(i)
        check = True
if check:
    lst.sort()
    print(*lst)
else:
    print(0)
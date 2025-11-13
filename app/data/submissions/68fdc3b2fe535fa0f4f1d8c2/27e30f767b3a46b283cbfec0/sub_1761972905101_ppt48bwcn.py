n = int(input())
array = list(map(int, input().split()))
check = False
for i in range(1,max(array)+1):
    if i not in array:
        print(i, end = ' ')
        check = True
if not check:
    print(5)
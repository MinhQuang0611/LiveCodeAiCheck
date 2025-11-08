n = int(input())
array = list(map(int, input().split()))
check = True
for i in range(1,max(array)+1):
    if i not in array:
        print(i)
        check = False
if check:
    print("Excellent!")
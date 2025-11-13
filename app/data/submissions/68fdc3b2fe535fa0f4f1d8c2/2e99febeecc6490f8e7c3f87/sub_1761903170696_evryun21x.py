n = int(input())
line = input()
arr = line.split()
arr1 = [x for x in range(1, int(arr[-1])+2)]
arr2 = []
for i in arr1:
    if str(i) not in arr:
        arr2.append(i)
print(min(arr2))
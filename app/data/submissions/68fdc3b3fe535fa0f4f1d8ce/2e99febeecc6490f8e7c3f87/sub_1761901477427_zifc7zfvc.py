n = int(input())
arr = []
for i in range(n):
    line = input()
    arr.append(line)
arr1 = []
for i in arr:
    if i not in arr1:
        arr1.append(i)
count = (len(arr1))
print(count)
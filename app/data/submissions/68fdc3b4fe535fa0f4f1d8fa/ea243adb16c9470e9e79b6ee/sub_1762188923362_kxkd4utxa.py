n = int(input())
arr = list(map(int, input().split()))
arr_snt = []

def snt(num):
    if n < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    else:
        return True

for i in range(n):
    if snt(arr[i]):
        arr_snt.append(arr[i])

arr_snt.sort()    

arr_index = 0
for i in range(n):
    if snt(arr[i]):
        arr[i] = arr_snt[arr_index]
        arr_index += 1
print(*arr)
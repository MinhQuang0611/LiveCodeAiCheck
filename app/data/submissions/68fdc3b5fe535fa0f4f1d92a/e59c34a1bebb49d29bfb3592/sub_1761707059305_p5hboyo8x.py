n = int(input())
arr = list(map(int,input().split()))
a = []
i = 1
count = 0
while i < max(arr):
    i += 1
    if i not in arr:
        a.append(i)
        count += 1
if count == 0:
    print("Excellent!")
else:
    print(*a)


n = int(input())
numbers = list(map(int, input().split()))
while len(numbers) < n:
    numbers += list(map(int, input().split()))
da_xuat_hien = set(x for x in numbers if x > 0)
if da_xuat_hien:
    max_num = max(da_xuat_hien)
else:
    max_num = 0
chua_xuat_hien = [i for i in range(1, max_num + 1) if i not in da_xuat_hien]
if chua_xuat_hien:
    for num in chua_xuat_hien:
        print(num)
else:
    print("Excellent!")
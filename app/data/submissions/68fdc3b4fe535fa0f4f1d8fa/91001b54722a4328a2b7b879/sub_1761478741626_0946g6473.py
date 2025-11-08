import math

def kiem_tra_nguyen_to(x):
    if x <= 1:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

n = int(input())
arr = list(map(int, input().split()))

so_nguyen_to = sorted([x for x in arr if kiem_tra_nguyen_to(x)])

ket_qua = []
index_so_nguyen_to = 0
for x in arr:
    if kiem_tra_nguyen_to(x):
        ket_qua.append(so_nguyen_to[index_so_nguyen_to])
        index_so_nguyen_to += 1
    else:
        ket_qua.append(x)

print(*ket_qua)

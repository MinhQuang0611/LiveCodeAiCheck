a = int(input())
so_luong=0
for i in range(1, a+1):
    i = str(i)
    for j in i:
        if j=='1':
            so_luong+=1
print(so_luong)
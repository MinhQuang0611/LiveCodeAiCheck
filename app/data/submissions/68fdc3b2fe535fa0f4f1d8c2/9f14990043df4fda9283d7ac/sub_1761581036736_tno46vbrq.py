n = map(int, input().split())
danh_sach = list(map(int, input().split()))
s = set(x for x in danh_sach if x > 0)
so = 1
while so in s:
    so += 1
print(so)
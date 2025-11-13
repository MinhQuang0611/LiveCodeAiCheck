n = int(input())
m = list(map(int, input().split()))
max_val = max(m)
min_val = min(m)
loc = [x for x in m if x != max_val and x != min_val]
tong = sum(loc)
tong_so = len(loc)
trung_binh = tong/tong_so
print(int(trung_binh))
n = int(input())
day_so = list(map(int, input().split()))
so_hieu = set(day_so)
so_min = 1
while so_min in so_hieu:
    so_min += 1
print(so_min)


n= int(input())
day_so = list(map(int, input().split()))
lon=max(day_so)
be=min(day_so)
s = [x for x in day_so if x !=max(day_so) and x != min(day_so)]
if s:
    trung_binh = sum(s) / len(s)
    print(int(trung_binh))
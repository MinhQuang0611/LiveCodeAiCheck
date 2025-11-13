n = int(input())
day_so = list(map(int, input().split()))
solonhat=max(day_so)
sobenhat=min(day_so)
day_moi = [x for x in day_so if x !=max(day_so) and x != min(day_so)]
if day_moi:
    trung_binh = sum(day_moi) / len(day_moi)
    print(int(trung_binh))
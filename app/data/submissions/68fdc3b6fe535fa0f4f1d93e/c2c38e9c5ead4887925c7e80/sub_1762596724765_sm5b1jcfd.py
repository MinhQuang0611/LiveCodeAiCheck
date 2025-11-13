n = int(input())
day_so = list(map(float,input().split()))
max_x = max(day_so)
min_x = min(day_so)
new_day_so = [x for x in day_so if x!= max_x and x != min_x]
trung_binh_cong = sum(new_day_so)/len(new_day_so)
print(round(trung_binh_cong))
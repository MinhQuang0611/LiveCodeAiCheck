n = int(input())
day_so= list(map(float, input().split()))
gtln = max(day_so)
gtnn = min(day_so)
phan_con_lai = [x for x in day_so if x != gtnn and x != gtln]
ketqua = sum(phan_con_lai) / len(phan_con_lai)
print(int(ketqua))
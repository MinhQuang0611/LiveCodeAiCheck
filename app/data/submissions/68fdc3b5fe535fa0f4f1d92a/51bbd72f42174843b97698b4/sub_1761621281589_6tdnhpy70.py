n = int(input())
cac_so = []
while len(cac_so) < n:
    cac_so.extend(map(int, input().split()))
max_so = max(cac_so)
tap_hop_so = set(cac_so)
so_thieu = []
for i in range(1, max_so + 1):
    if i not in tap_hop_so:
        so_thieu.append(i)
if not so_thieu:
    print("Excellent!")
else:
    for so in so_thieu:
        print(so)
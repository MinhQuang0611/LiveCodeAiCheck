n, k = map(int, input().split())
a = list(map(int, input().split()))

tudien = {}

for i in a:
    if i not in tudien:
        tudien[i] = 1
    else:
        tudien[i] += 1
tansuat = sorted(set(tudien.values()), reverse=True)
#print(*tansuat)
if len(tansuat) < 2:
    print("NONE")
else:
    muc2 = tansuat[1]
    ketqua = [x for x in tudien if tudien[x] == muc2]
    print(*ketqua)

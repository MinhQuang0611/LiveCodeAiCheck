a = int(input())
tong = {}
s =[]
for _ in range(a):
    ten =input().strip()
    sta =input().strip()
    en = input().strip()
    luong_mua = int(input())
    h1, m1 = map(int, sta.split(":"))
    h2, m2 = map(int,en.split(":"))
    thoi_gian = (h2*60+m2)-(h1*60+m1)
    if ten not in tong:
        tong[ten] = [0,0]
        s.append(ten)
    tong[ten][0] += thoi_gian
    tong[ten][1] += luong_mua
for i, ten in enumerate(s,1):
    tong_tg,tong_mua = tong[ten]
    if tong_tg ==0:
        tb =0
    else:
        tb = tong_mua * 60 / tong_tg
    print(f"T{i:02} {ten} {tb:.2f}")
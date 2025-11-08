dai, rong, mau = input().split()
dai, rong = int(dai), int(rong)
if dai > 0 and rong > 0:
    chu_vi = (dai + rong)*2
    dien_tich = dai * rong
    print(chu_vi,dien_tich,mau.title())
else:
    print('INVALID')
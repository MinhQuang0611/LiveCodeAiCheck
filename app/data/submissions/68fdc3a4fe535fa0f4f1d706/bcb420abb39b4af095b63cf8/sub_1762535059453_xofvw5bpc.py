import math
t=int(input())
ds_ket_qua=[]
for i in range(t):
    x1,y1,x2,y2=map(int,input().split())
    khoang_cach=math.sqrt((x2-x1)**2+(y2-y1)**2)
    khoang_cach_round=f"{khoang_cach:.4f}"
    ds_ket_qua+=[khoang_cach_round]
for o in ds_ket_qua:
    print(o)
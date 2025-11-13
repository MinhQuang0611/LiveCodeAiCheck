n=int(input())
sap_xep=[]
for i in range (1,n+1):
    name=input()
    d1=float(input())
    d2=float(input())
    if d1>10 or d2>10:
        d1=d1/10
        d2=d2/10
    trung_binh=(d1+d2)/2
    if trung_binh < 5:
        phan_loai="TRUOT"
    elif trung_binh > 5 and trung_binh <= 8:
        phan_loai="CAN NHAC"
    elif trung_binh > 8 and trung_binh < 9.5:
        phan_loai = "DAT"
    elif trung_binh >= 9.5:
        phan_loai = "XUAT SAC"
    sap_xep.append((f'TS0{i}',name,trung_binh,phan_loai))
sap_xep = sorted(sap_xep, key=lambda x: x[2], reverse=True)
for i, name, trung_binh, phan_loai in sap_xep:
    print(f'{i} {name} {trung_binh:.2f} {phan_loai}')

t=int(input())
ds=[]
for i in range(1,t+1):
    name=input().strip()
    a,b=float(input()),float(input())
    if a>10:
        a/=10
    if b>10:
        b/=10
    kq=round((a+b)/2,2)
    if kq>=9.5:
        s2="XUAT SAC"
    elif kq>=8:
        s2="DAT"
    elif kq>=5:
        s2="CAN NHAC"
    else:
        s2="TRUOT"
    ds.append((i,name,kq,s2))
ds.sort(key=lambda x:-x[2])
for i,name,kq,s2 in ds:
    print(f"TS{i:02d} {name} {kq:.2f} {s2}")

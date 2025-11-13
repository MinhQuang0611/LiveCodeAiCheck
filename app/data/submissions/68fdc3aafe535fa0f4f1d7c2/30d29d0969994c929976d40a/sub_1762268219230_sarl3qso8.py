a=input()
danh_sach=set()
for i in range(0,len(a),2):
    so=a[i:i+2]
    danh_sach.add(so)
ketqua=sorted(danh_sach)
print(" ".join(ketqua))

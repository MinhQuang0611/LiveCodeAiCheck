n=int(input())
tb=float(0)
nhap=input()
parts=nhap.split()
for i in parts:
    tb+=float(i)
tb/=n
print("%.2f"%round(tb,2))
if tb>= 8.5: print("Xuất sắc")
elif tb>=7: print("Giỏi")
elif tb>=5.5: print("Khá")
elif tb>=4: print("Trung bình")
else: print("Yếu")
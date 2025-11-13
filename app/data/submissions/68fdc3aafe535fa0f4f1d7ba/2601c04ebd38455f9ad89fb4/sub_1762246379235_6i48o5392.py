chuoi = input("Nhập chuỗi: ").strip()
la_ky_dieu = True
for i in range(2, len(chuoi)):
    if chuoi[i] != chuoi[i - 2]:
        la_ky_dieu = False
        break
if la_ky_dieu:
    print("YES")
else:
    print("NO")

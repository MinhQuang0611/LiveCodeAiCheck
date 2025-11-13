n = input("nhap so: ")
dem = 0
while True:
    dem += 1
    tong = sum(int(i) for i in n)
    if tong < 10:
        print("so sau do la:", dem)
        break
    n = str(tong)

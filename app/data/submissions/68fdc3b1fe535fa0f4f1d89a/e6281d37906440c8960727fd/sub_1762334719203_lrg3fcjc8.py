n = input("birth: ")
dem = 0

while True:
    tong = sum(int(i) for i in n)
    dem += 1
    if tong < 10:
        print("core:", tong)
        print("times:", dem)
        break
    n = str(tong)
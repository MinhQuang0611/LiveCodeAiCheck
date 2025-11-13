n = input()
dem = 0

while True:
    tong = sum(int(i) for i in n)
    dem += 1
    if tong < 10:
        print(dem)
        break
    n = str(tong)
n = input("nhập số:")
while True:
    tong = sum(int(i) for i in n)
    if tong < 10:
        print("số cần tìm là:", tong)
        break
    n = str(tong)    
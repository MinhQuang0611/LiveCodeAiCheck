ngay = int(input())
thang = int(input())

if (thang == 3 and ngay >= 21) or (thang == 4 and ngay <= 19):
    print("Bạch Dương")
elif (thang == 4 and ngay >= 20) or (thang == 5 and ngay <= 20):
    print("Kim Ngưu")
elif (thang == 5 and ngay >= 21) or (thang == 6 and ngay <= 20):
    print("Song Tử")
elif (thang == 6 and ngay >= 21) or (thang == 7 and ngay <= 22):
    print("Cự Giải")
elif (thang == 7 and ngay >= 23) or (thang == 8 and ngay <= 22):
    print("Sư Tử")
elif (thang == 8 and ngay >= 23) or (thang == 9 and ngay <= 22):
    print("Xử Nữ")
elif (thang == 9 and ngay >= 23) or (thang == 10 and ngay <= 22):
    print("Thiên Bình")
elif (thang == 10 and ngay >= 23) or (thang == 11 and ngay <= 21):
    print("Bọ Cạp")
elif (thang == 11 and ngay >= 22) or (thang == 12 and ngay <= 21):
    print("Nhân Mã")
elif (thang == 12 and ngay >= 22) or (thang == 1 and ngay <= 19):
    print("Ma Kết")
elif (thang == 1 and ngay >= 20) or (thang == 2 and ngay <= 18):
    print("Bảo Bình")
elif (thang == 2 and ngay >= 19) or (thang == 3 and ngay <= 20):
    print("Song Ngư")
t=int(input())
i=0
while i!=t:
        ngay_sinh ,thang_sinh = map(int,input().split())

        if(22<=ngay_sinh<=31 and thang_sinh==12) or (1<=ngay_sinh<=19 and thang_sinh==1):
            print("Ma Ket")
        elif(20<=ngay_sinh<=31 and thang_sinh==1) or (1<=ngay_sinh<=18 and thang_sinh==2):
            print("Bao Binh")
        elif(19<=ngay_sinh<=29 and thang_sinh==2) or (1<=ngay_sinh<=20 and thang_sinh==3):
            print("Song Ngu")
        elif(21<=ngay_sinh<=31 and thang_sinh==3) or (1<=ngay_sinh<20 and thang_sinh==4):
            print("Bach Duong")         
        elif(20<=ngay_sinh<=30 and thang_sinh==4) or (1<=ngay_sinh<=20 and thang_sinh==5):
            print("Kim Nguu")
        elif(21<=ngay_sinh<=31 and thang_sinh==5) or (1<=ngay_sinh<=21 and thang_sinh==6):
            print("Song Tu")
        elif(22<=ngay_sinh<=30 and thang_sinh==6) or (1<=ngay_sinh<=22 and thang_sinh==7):
            print("Cu Giai")
        elif(23<=ngay_sinh<=31 and thang_sinh==7) or (1<=ngay_sinh<=22 and thang_sinh==8):
            print("Su Tu")
        elif(23<=ngay_sinh<=31 and thang_sinh==8) or (1<=ngay_sinh<=22 and thang_sinh==9):
            print("Xu Nu")
        elif(23<=ngay_sinh<=30 and thang_sinh==9) or (1<=ngay_sinh<=23 and thang_sinh==10):
            print("Thien Binh")
        elif(24<=ngay_sinh<=31 and thang_sinh==10) or (1<=ngay_sinh<=22 and thang_sinh==11):
            print("Thien Yet")
        elif(23<=ngay_sinh<=30 and thang_sinh==11) or (1<=ngay_sinh<=21 and thang_sinh==12):
            print("Nhan Ma")
        i=i+1
t = int(input())
for i in range(t):
    d,m=map(int, input().split())
    if (d >= 22 and m == 12) or (d<=19 and m == 1) :
        print('Ma Ket')
    if (d >= 20 and m == 1) or (d<=18 and m == 2):
        print("Bao Binh")
    if (d >=19 and m == 2) or (d<=20 and m == 3):
        print('Song Ngu')
    if (d >=21 and m == 3) or (d<=19 and m == 4):
        print('Bach Duong')
    if (d >=20 and m == 4) or (d<=20 and m == 5):
        print('Kim Nguu')
    if (d >=21 and m == 5) or (d<=20 and m == 6):
        print('Song Tu')
    if (d >=21 and m == 6) or (d<=22 and m == 7):
        print('Cu Giai')
    if (d >=23 and m == 7) or (d<=22 and m == 8):
        print('Su Tu')
    if (d >=23 and m == 8) or (d<=22 and m == 9):
        print('Xu Nu')
    if (d >=23 and m == 9) or (d<=22 and m == 10):
        print('Thien Binh')
    if (d >=23 and m == 10) or (d<=22 and m == 11):
        print('Thien Yet')
    if (d >=23 and m == 11) or (d<=21 and m == 12):
        print('Nhan Ma')

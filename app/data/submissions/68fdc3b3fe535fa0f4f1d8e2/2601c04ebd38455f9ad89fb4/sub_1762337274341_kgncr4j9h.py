t = int(input())
for i in range(t):
    d, m = map(int, input().split())
    if (m == 12 and d >= 22) or (m == 1 and d <= 19):
        cung = "Ma Ket"
    elif (m == 1 and d >= 20) or (m == 2 and d <= 18):
        cung = "Bao Binh"
    elif (m == 2 and d >= 19) or (m == 3 and d <= 20):
        cung= "Song Ngu"
    elif (m == 3 and d >= 21) or (m == 4 and d <= 19):
        cung = "Bach Duong"
    elif (m == 4 and d >= 20) or (m == 5 and d <= 20):
        cung = "Kim Nguu"
    elif (m == 5 and d >= 21) or (m == 6 and d <= 20):
        cung = "Song Tu"
    elif (m == 6 and d >= 21) or (m == 7 and d <= 22):
        cung = "Cu Giai"
    elif (m == 7 and d >= 23) or (m == 8 and d <= 22):
        cung = "Su Tu"
    elif (m == 8 and d >= 23) or (m == 9 and d <= 22):
        cung = "Xu Nu"
    elif (m == 9 and d >= 23) or (m == 10 and d <= 22):
        cung= "Thien Binh"
    elif (m == 10 and d >= 23) or (m == 11 and d <= 21):
        cung = "Thien Yet"
    else:
        cung = "Nhan Ma"
    print(cung)

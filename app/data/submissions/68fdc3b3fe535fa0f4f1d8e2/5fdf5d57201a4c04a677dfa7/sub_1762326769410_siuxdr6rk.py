t = int(input())
ngaythang = []

for i in range(t):
    d, m = map(int, input().split())
    ngaythang.append((d, m))

for d, m in ngaythang:
    if t < 1 or t > 1000 or d < 1 or m < 1 or d > 31 or m > 12:
        exit()
    if (m == 12 and d >= 22) or (m == 1 and d <= 19):
        chomsao = "Ma Ket"
    elif (m == 1 and d >= 20) or (m == 2 and d <= 18):
        chomsao = "Bao Binh"
    elif (m == 2 and d >= 19) or (m == 3 and d <= 20):
        chomsao = "Song Ngu"
    elif (m == 3 and d >= 21) or (m == 4 and d <= 19):
        chomsao = "Bach Duong"
    elif (m == 4 and d >= 20) or (m == 5 and d <= 20):
        chomsao = "Kim Nguu"
    elif (m == 5 and d >= 21) or (m == 6 and d <= 20):
        chomsao = "Song Tu"
    elif (m == 6 and d >= 21) or (m == 7 and d <= 22):
        chomsao = "Cu Giai"
    elif (m == 7 and d >= 23) or (m == 8 and d <= 22):
        chomsao = "Su Tu"
    elif (m == 8 and d >= 23) or (m == 9 and d <= 22):
        chomsao = "Xu Nu"
    elif (m == 9 and d >= 23) or (m == 10 and d <= 22):
        chomsao = "Thien Binh"
    elif (m == 10 and d >= 23) or (m == 11 and d <= 22):
        chomsao = "Thien Yet"
    else:
        chomsao = "Nhan Ma"

    print(chomsao)

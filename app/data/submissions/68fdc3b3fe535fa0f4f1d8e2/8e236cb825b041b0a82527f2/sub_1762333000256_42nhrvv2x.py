from datetime import date


def chom_sao(d, m):
    y = 1999 if m == 12 and d >= 22 else 2000
    day = date(y, m, d)
    if date(1999, 12, 22) <= day <= date(2000, 1, 19):
        return "Ma Ket"
    if date(2000, 1, 20) <= day <= date(2000, 2, 18):
        return "Bao Binh"

    if date(2000, 2, 19) <= day <= date(2000, 3, 20):
        return "Song Ngu"

    if date(2000, 3, 21) <= day <= date(2000, 4, 19):
        return "Bach Duong"

    if date(2000, 4, 20) <= day <= date(2000, 5, 20):
        return "Kim Nguu"

    if date(2000, 5, 21) <= day <= date(2000, 6, 20):
        return "Song Tu"

    if date(2000, 6, 21) <= day <= date(2000, 7, 22):
        return "Cu Giai"

    if date(2000, 7, 23) <= day < date(2000, 8, 22):
        return "Su Tu"

    if date(2000, 8, 23) <= day <= date(2000, 9, 22):
        return "Xu Nu"

    if date(2000, 9, 23) <= day <= date(2000, 10, 22):
        return "Thien Binh"

    if date(2000, 10, 23) <= day <= date(2000, 11, 22):
        return "Thien Yet"

    if date(2000, 11, 23) <= day <= date(2000, 12, 21):
        return "Nhan Ma"


t = int(input())
for _ in range(t):
    d, m = map(int, input().split())
    print(chom_sao(d, m))

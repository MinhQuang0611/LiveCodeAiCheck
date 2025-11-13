n = int(input().strip())
for _ in range(n):
    day, month = map(int, input().strip().split())

    if (month == 12 and day >= 22) or (month == 1 and day <= 19):
        print("Ma Ket", end="")
    elif (month == 1 and day >= 20) or (month == 2 and day <= 18):
        print("Bao Binh", end="")
    elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
        print("Song Ngu", end="")
    elif (month == 3 and day >= 21) or (month == 4 and day <= 19):
        print("Bach Duong", end="")
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        print("Kim Nguu", end="")
    elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
        print("Song Tu", end="")
    elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
        print("Cu Giai", end="")
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        print("Su Tu", end="")
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
        print("Xu Nu", end="")
    elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
        print("Thien Binh", end="")
    elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
        print("Bo Cap", end="")
    elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
        print("Nhan Ma", end="")
    
    if _ != n - 1:
        print()
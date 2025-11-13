chu_so = int(input())
while chu_so > 0:
    n = list(map(int, input().split()))
    if n[1] == 12 and n[0] > 21 and n[0] < 32 or n[1] == 1 and n[0] > 0 and n[0] < 20 :
        print('Ma Ket')
    elif n[1] == 1 and n[0] > 0 and n[0] < 21 or n[1] == 2 and n[0] > 0 and n[0] < 19 :
        print('Bao Binh')
    elif n[1] == 2 and n[0] > 18 and n[0] < 30 or n[1] == 3 and n[0] > 0 and n[0] < 21 :
        print('Song Ngu')
    elif n[1] == 3 and n[0] > 20 and n[0] < 32 or n[1] == 4 and n[0] > 0 and n[0] < 20 :
        print('Bach Duong')
    elif n[1] == 4 and n[0] >19 and n[0] < 31 or n[1] == 5 and n[0] > 0 and n[0] < 21 :
        print('Kim Nguu')
    elif n[1] == 5 and n[0] > 20 and n[0] < 32 or n[1] == 6 and n[0] > 0 and n[0] < 21 :
        print('Song Tu')
    elif n[1] == 6 and n[0] > 20 and n[0] < 31 or n[1] == 7 and n[0] > 0 and n[0] < 21 :
        print('Cu Giai')
    elif n[1] == 7 and n[0] > 22 and n[0] < 32 or n[1] == 8 and n[0] > 0 and n[0] < 23 :
        print('Su Tu')
    elif n[1] == 8 and n[0] > 22 and n[0] < 32 or n[1] == 9 and n[0] > 0 and n[0] < 23 :
        print('Su Nu')
    elif n[1] == 9 and n[0] > 22 and n[0] < 31 or n[1] == 10 and n[0] > 0 and n[0] < 23 :
        print('Thien Binh')
    elif n[1] == 10 and n[0] > 22 and n[0] < 32 or n[1] == 11 and n[0] > 0 and n[0] < 23 :
        print('Thien Yet')
    else :
        print('Nhan Ma')
    chu_so -=1
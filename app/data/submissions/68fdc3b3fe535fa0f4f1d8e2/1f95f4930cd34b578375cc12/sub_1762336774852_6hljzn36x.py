n = int(input())
a = []
b = []
for i in range(n):
    k, h = map(int, input().split())
    a.append(k)
    b.append(h)

for i in range(n):
    if a[i] <= 19 and b[i] == 1:
        print('Ma Ket')
    elif a[i] > 19 and b[i] == 1:
        print('Bao Binh')
    elif a[i] <= 18 and b[i] == 2:
        print('Bao Binh')
    elif a[i] > 18 and b[i] == 2:
        print('Song Ngu') 
    elif a[i] <= 20 and b[i] == 3:
        print('Song Ngu')
    elif a[i] > 20 and b[i] == 3:
        print('Bach Duong')
    elif a[i] <= 19 and b[i] == 4:
        print('Bach Duong')
    elif a[i] > 19 and b[i] == 4:
        print('Kim Nguu')
    elif a[i] <= 20 and b[i] == 5:
        print('Kim Nguu')
    elif a[i] > 20 and b[i] == 5:
        print('Song Tu')
    elif a[i] <= 20 and b[i] == 6:
        print('Song Tu')
    elif a[i] > 20 and b[i] == 6:
        print('Cu Giai')
    elif a[i] <= 22 and b[i] == 7:
        print('Cu Giai')
    elif a[i] > 22 and b[i] == 7:
        print('Su Tu')
    elif a[i] <= 22 and b[i] == 8:
        print('Su Tu')
    elif a[i] > 22 and b[i] == 8:
        print('Xu Nu')
    elif a[i] <= 22 and b[i] == 9:
        print('Xu Nu')
    elif a[i] > 22 and b[i] == 9:
        print('Thien Binh')
    elif a[i] <= 22 and b[i] == 10:
        print('Thien Binh')
    elif a[i] > 22 and b[i] == 10:
        print('Thien Yet')
    elif a[i] <= 22 and b[i] == 11:
        print('Thien Yet')
    elif a[i] > 22 and b[i] == 11:
        print('Nhan Ma')
    elif a[i] <= 21 and b[i] == 12:
        print('Nhan Ma')
    elif a[i] > 21 and b[i] == 12:
        print('Ma Ket')
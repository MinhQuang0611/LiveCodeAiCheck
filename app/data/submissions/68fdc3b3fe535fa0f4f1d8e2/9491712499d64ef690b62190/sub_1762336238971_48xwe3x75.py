t=int(input())
if (t < 1 or t > 1000):
    print('Khong hop le')
cung=[]
c=1
while c<=t:
    d, m = map(int, input().split())
    if (m < 1 or m > 12) or (d < 1 or d > 31):
        break
    if (m == 12 and d >= 22) or (m == 1 and d <= 19):
        a=("Ma Ket")
    elif (m == 1 and d >= 20) or (m == 2 and d <= 18):
        a=("Bao Binh")
    elif (m == 2 and d >= 19) or (m == 3 and d <= 20):
        a=("Song Ngu")
    elif (m == 3 and d >= 21) or (m == 4 and d <= 19):
        a=("Bach Duong")
    elif (m == 4 and d >= 20) or (m == 5 and d <= 20):
        a=("Kim Nguu")
    elif (m == 5 and d >= 21) or (m == 6 and d <= 20):
        a=("Song Tu")
    elif (m == 6 and d >= 21) or (m == 7 and d <= 22):
        a=("Cu Giai")
    elif (m == 7 and d >= 23) or (m == 8 and d <= 22):
        a=("Su Tu")
    elif (m == 8 and d >= 23) or (m == 9 and d <= 22):
        a=("Xu Nu")
    elif (m == 9 and d >= 23) or (m == 10 and d <= 22):
        a=("Thien Binh")
    elif (m == 10 and d >= 23) or (m == 11 and d <= 22):
        a=("Thien Yet")
    elif (m == 11 and d >= 23) or (m == 12 and d <= 21):
        a=("Nhan Ma")
    else:
        print("Khong hop le")
    cung.append(a)
    c+=1
for i in range(t):
        print(cung[i])
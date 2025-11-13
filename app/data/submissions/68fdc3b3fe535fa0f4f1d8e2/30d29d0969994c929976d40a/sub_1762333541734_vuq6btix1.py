def ngaythang(d,m):
    if (d>=22 and m==12) or (d<=19 and m==1):
        return "Ma Ket" 
    if (d>=20 and m==1) or(d<=18 and m==2):
        return "Bao Binh"
    if (d>=19 and m==2) or (d<=20 and m==3):
        return "Song Ngu"
    if (d>=21 and m==3) or (d<=19 and m==4):
        return "Bach Duong"
    if (d>=20 and m==4) or (d<=20 and m==5):
        return "Kim Nguu" 
    if (d>=21 and m==5) or (d<=20 and m==6):
        return "Song Tu" 
    if (d>=21 and m==6) or (d<=22 and m==7):
        return "Cu Giai"
    if (d>=23 and m==7) or (d<=22 and m==8):
        return "Su Tu" 
    if (d>=23 and m==8) or (d<=22 and m==9):
        return "Xu Nu"
    if (d>=23 and m==9) or (d<=22 and m==10):
        return "Thien Binh"
    if (d>=23 and m==10) or (d<=22 and m==11):
        return "Thien Yet"
    if (d>=23 and m==11) or (d<=21 and m==12):
        return "Nhan Ma" 
n=int(input())
for _ in range(1,n+1):
    d, m=map(int,input().split())
    print(ngaythang(d,m))
def tim_chom_sao(d,m):
    if m==1:
        return "Ma Ket" if d <=19 else "Bao Binh"
    elif m==2:
        return "Bao Binh" if d <=18 else "Song Ngu"
    elif m ==3:
        return "Song Ngu" if d <=20 else "Bach Duong"
    elif m==4:
        return "Bach Duong" if d<=19 else "Kim Nguu"
    elif m==5:
        return "Kim Nguu" if d<=20 else "Song Tu"
    elif m==6:
        return "Song Tu" if d<=20 else "Cu Giai"
    elif m ==7:
        return "Cu Giai" if d<=22 else "Su Tu"
    elif m==8:
        return "Su Tu" if d<= 22 else "Xu Nu"
    elif m==9:
        return "Xu Nu" if d <=22 else "Thien Binh"
    elif m==10:
        return "Thien Binh" if d<=22 else "Thien Yet"
    elif m ==11:
        return "Thien Yet" if d<=22 else "Nhan Ma"
    elif m==12:
        return "Nhan Ma" if d<=21 else "Ma Ket"
t = int(input())
for _ in range(t):
    v,s = map(int,input().split())
    print(tim_chom_sao(v,s))

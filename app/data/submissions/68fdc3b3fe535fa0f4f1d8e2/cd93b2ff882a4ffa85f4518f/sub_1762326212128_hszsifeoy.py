n=int(input())
for _ in range (n):
    d,m=map(int, input().split())
    if (d>=22 and m==12) or (m==1 and d<=19):
        print("Ma Ket")
    elif (d>=20 and m==1) or (m==2 and d<=18):
        print("Bao Binh")
    elif (d>=19 and m==2) or (m==3 and d<=20):
        print("Song Ngu")
    elif (d>=21 and m==3) or (m==4 and d<=19):
        print("Bach Duong")
    elif (d>=20 and m==4) or (m==5 and d<=20):
        print("Kim Nguu")
    elif (d>=21 and m==5) or (m==6 and d<=20):
        print("Song Tu")
    elif (d>=21 and m==6) or (m==7 and d<=22):
        print("Cu Giai")
    elif (d>=23 and m==7) or (m==8 and d<=22):
        print("Su Tu")  
    elif (d>=23 and m==8) or (m==9 and d<=22):
        print("Xu Nu")  
    elif (d>=23 and m==9) or (m==10 and d<=22):
        print("Thien Binh") 
    elif (d>=23 and m==10) or (m==11 and d<=22):
        print("Thien Yet")
    else:
        print("Nhan Ma") 
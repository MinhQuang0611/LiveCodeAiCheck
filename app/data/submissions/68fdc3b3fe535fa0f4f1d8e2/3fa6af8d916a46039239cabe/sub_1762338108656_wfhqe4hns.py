t=int(input())
while t:
    t-=1
    d,m=map(int,input().split())
    if (m==12 and 22<=d<=31) or (m==1 and 1<=d<=19):
        print("Ma Ket")
    elif (m==1 and 20<=d<=31) or (m==2 and 1<=d<=18):
        print("Bao Binh")
    elif (m==2 and 19<=d<=29) or (m==3 and 1<=d<=20):
        print("Song Ngu")
    elif (m==3 and 21<=d<=31) or (m==4 and 1<=d<=19):
        print("Bach Duong")
    elif (m==4 and 20<=d<=30) or (m==5 and 1<=d<=20):
        print("Kim Nguu")
    elif (m==5 and 21<=d<=31) or (m==6 and 1<=d<=20):
        print("Song Tu")
    elif (m==6 and 21<=d<=30) or (m==7 and 1<=d<=22):
        print("Cu Giai")
    elif (m==7 and 23<=d<=31) or (m==8 and 1<=d<=22):
        print("Su Tu")
    elif (m==8 and 23<=d<=31) or (m==9 and 1<=d<=22):
        print("Xu Nu")
    elif (m==9 and 23<=d<=30) or (m==10 and 1<=d<=22):
        print("Thien Binh")
    elif (m==10 and 23<=d<=31) or (m==11 and 1<=d<=22):
        print("Thien Yet")
    elif (m==11 and 23<=d<=30) or (m==12 and 1<=d<=21):
        print("Nhan Ma")
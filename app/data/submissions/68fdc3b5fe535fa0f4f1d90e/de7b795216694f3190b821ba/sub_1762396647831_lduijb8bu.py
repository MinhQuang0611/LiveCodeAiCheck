so_luong_so=int(input())
i=0
tich=1
tong=0
h=0
while i!=so_luong_so:
        so=str(input())
        while h!=len(so):
                if h%2!=0 and so[h]!="0":
                       tong=tong+int(so[h])
                 #       tich=tich*int(so[h])
                elif h%2== 0:
                #        tong=tong+int(so[h])
                       tich=tich*int(so[h])
                h=h+1
        print(tich, tong,)
        tich=1
        tong=0  
        h=0
        i=i+1


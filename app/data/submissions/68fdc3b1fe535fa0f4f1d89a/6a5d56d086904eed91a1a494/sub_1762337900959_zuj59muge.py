n = input()
so = int(n)
pt = list(n)
sl = len(pt)
tam = 0
dem = 0

while (so > 10):
    for num in pt:
        tam = tam+int(num)
    so = tam
    tam = 0
    pt = list(str(so))
    dem = dem +1
        
print(dem)
 

    


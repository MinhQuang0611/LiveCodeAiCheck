n = int(input())
ds = input()
ds = ds.split()
sl = len(ds)
sln = 1
snn = 1000000
dem = 0
for i in range(0,sl):
    tam = int(ds[i])
    ds[i] = tam
    if sln < tam:
        sln = tam
    if snn > tam:
        snn = tam
ds1 = set(ds)
for j in range(snn,sln):
    if j not in ds1:
        print(j)
        dem = 1
if dem == 0:
    print("Excellent!")


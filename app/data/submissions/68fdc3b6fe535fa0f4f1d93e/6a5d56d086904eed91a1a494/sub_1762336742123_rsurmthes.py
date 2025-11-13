n = int(input())
ds = input()
ds = list(map(int,ds.split()))
ln = - 9999999
nn = 9999999
tong = 0
sl = n
for i in range(0,n):
    
    if ds[i] < nn:
        nn = ds[i]
    if ds[i] > ln:
        ln = ds[i]
for j in range(0,n):
    if (ds[j] == nn):
        ds[j] = 0 
        sl = sl -1
    
    if (ds[j] == ln):
        ds[j] =0
        sl = sl -1
        
    
    tong = tong+ds[j]
tb = tong / sl
print(f"{tb:g}")

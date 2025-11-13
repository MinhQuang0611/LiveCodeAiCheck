n = input()
ds = list(n)
sl = len(ds) 
kytu = [',', ':', ' '] 
i = 0
dem = 0
while (i < sl):
    
   
    while i < sl and ds[i].isalnum() == False and ds[i] not in kytu:
        
        del ds[i]
        sl = sl - 1
    if i >= sl:
        break 
    if ds[i].isalpha() == True:
        ds[i] = ds[i].lower()
    i = i + 1
for j in range(0,sl):
    if dem == 1:
        dem = 0
        ds[j] = ds[j].upper()
    if ds[j] == ' ':
        dem = 1
if (ds[0].islower() == True):
    ds[0] = ds[0].upper()

ds = ''.join(ds)
ds = ds.split()
ds = ' '.join(ds)
print(ds)
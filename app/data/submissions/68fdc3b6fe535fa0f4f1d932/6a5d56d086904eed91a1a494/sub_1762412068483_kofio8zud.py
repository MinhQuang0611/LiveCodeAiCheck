nm = input()
db = list(nm)
n = int(db[0])

tv = {}
def snt(chuoi):
    ds = chuoi.split()
    sl = len(ds)
    for i in range(0,sl):
        a= 1
        tam = int(ds[i])
        if (tam == 1) or (tam == 0):
            print(0,end=' ')
            continue
        if (tam == 2) or (tam == 3):
            print(1,end=' ')
            continue
        for j in range(2,tam):
            if tam % j == 0:
                print(0,end=' ')
                a = 0
                break
        if a == 1:
            print(1,end=' ')
    print('')

for i in range (0,n):
    tv[i] = input()
for j in range(0,n):
    snt(tv[j])
    

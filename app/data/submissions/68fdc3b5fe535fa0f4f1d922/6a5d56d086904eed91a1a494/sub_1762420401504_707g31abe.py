n = int(input())
ds = [0] * n
slkt = 0
a =0
kt = {
}

for i in range(0,n) :
    ds[i] = input()
for j in range(0,n):
    tam = list(ds[j])
    sl = len(tam)
    for k in range(0,sl):
        if tam[k] == '(':
            slkt += 1
            print(slkt,end = ' ')
            kt[slkt] = True
            
        if tam[k] == ')':
            for l in range(slkt,0,-1):
                if (kt[l] == True):
                    print(l,end= ' ')
                    kt[l] = False
                    break
    slkt = 0
                    

    
    print('')



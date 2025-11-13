n = int(input())
tv = {}
ds = [0] * n
slt =0

def tt(a,b,c):
    ds1 = a.split(':')
    ds2 = b.split(':')
    no =0
    if (int(ds2[1]) > int(ds1[1])):
        p2 = (int(ds2[1]) - int(ds1[1]))/60
    else:    
        p2 = (60 - int(ds2[1]) + int(ds1[1]))/60
        no = 1
    p1 = int(ds2[0]) - int(ds1[0])
    tb =  c/(p2 + p1 - no)
    
    return tb





for i in range(0,n):
    ten = input()
    ds[slt] = ten
    tv[slt] = {
        'bd' : 0,
        'kt' : 0,
        'lm' : 0
    }
    tv[slt]['bd'] = input()
    tv[slt]['kt'] = input()
    tv[slt]['lm'] = int(input())
    slt = slt+1
a=0
for j in range(0,slt):
    a = a+1
    if (a < 10):
        print('T',end='')
        print(0,end='')
        print(a,end =' ')
    else:
        print('T',end=' ')
        print(a)
    ten = ds[j]
    print(ten,end =' ')
    kq = tt(tv[j]['bd'],tv[j]['kt'],tv[j]['lm'])
    print(f"{kq:.2f}")
    
    


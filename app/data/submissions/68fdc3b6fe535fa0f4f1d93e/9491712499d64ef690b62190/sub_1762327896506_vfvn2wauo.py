a=int(input())
so= input()
cacso= list(map(int, so.split()))
while True :
    if len(cacso)>=3 and len(cacso)<=10**5:
        cacso.remove(min(cacso))
        cacso.remove(max(cacso))
        cacsosau=len(cacso)
        tong=0
        for s in cacso:
            tong+=s
        kq=round(float((tong)/(cacsosau)),2)
        print(kq)
    else:
        print('khong hop le')
    break
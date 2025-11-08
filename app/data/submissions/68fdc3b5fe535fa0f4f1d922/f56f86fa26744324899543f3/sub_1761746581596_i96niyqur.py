a=int(input())
b=[]
for i  in range(a):
    b.append(input())
for i in b:
    phai=trai=0
    for j in i:
        if j=="(":
            phai+=1
            trai+=1
            trai=phai
            print(phai,end=' ')
        elif j==")":
            print(trai,end=' ')
            trai-=1
    print("")

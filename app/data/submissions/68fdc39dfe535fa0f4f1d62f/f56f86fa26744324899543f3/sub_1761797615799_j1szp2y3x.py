a=[[3,4],[5,6],[7,9],[10,12],[13,15],[16,19],[20,22],[23,26],[27,29],[30,32],[33,34],[35,36],[37,38],[39,40]]
b=[2.5,3.0,3.5,4.0,4.5,5.0,5.5,6.0,6.5,7.0,7.5,8.0,8.5,9.0]
a1=int(input())
b1=[]
for i in range(a1):
    b1.append(list(map(float,input().split())))
for j in b1:
    for i in range(len(a)):
        if j[0] >=a[i][0] and j[0]<=a[i][1]:j[0]=b[i]
        if j[1] >=a[i][0] and j[1]<=a[i][1]:j[1]=b[i]
    a2=sum(j)/4
    a3=a2-int(a2)
    if a3>=0.75:print(float(int(a2))+1)
    elif a3>=0.25:print(float(int(a2))+0.5)
    else:print(float(int(a2)))

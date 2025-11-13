import math
b=[]
a=int(input())
for i in range(a):
    b.append(list(map(float,input().split())))
for i in b:
    c1=math.log(i[2]/i[0],(1+i[1]/100))
    if type(c1)==int:print(c1,end=' ')
    else:print(int(c1)+1,end=' ')

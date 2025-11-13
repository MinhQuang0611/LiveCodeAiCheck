n=int(input())
a=input()
b=input()
c=input()
chua1=[]
chua2=[]
chua3=[]
for i in a:
    chua1.append(i)
if chua1[0]==chua1[-1]:
    print('YES')
else:
    print('NO')
for i in b:
    chua2.append(i)
if chua2[0]==chua2[-1]:
    print('YES')
else:
    print('NO')
for i in c:
    chua3.append(i)
if chua3[0]==chua3[-1]:
    print('YES')
else:
    print('NO')
n=input()
a=input().strip()
b=input().strip()
c=input().strip()
b1=[]
b2=[]
b3=[]
for i in a:
    b1.append(i)
if b1[0]==b1[-1]:
    print('YES')
else:
    print('NO')
for i in b:
    b2.append(i)
if b2[0]==b2[-1]:
    print('YES')
else:
    print('NO')
for i in c:
    b3.append(i)
if b3[0]==b3[-1]:
    print('YES')
else:
    print('NO')
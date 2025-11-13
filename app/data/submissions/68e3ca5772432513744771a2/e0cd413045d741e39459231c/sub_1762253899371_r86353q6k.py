n=int(input())
digits=eval(input())
a=[]
ngoai=[]
while n>0:
    du=n%10
    a.append(du)
    n//=10
for i in a:
    if i in digits:
        continue
    else:
        ngoai.append(i)
if ngoai==[] and a==a[::-1]:
    print('True')
else:
    print('False')
b=int(input())
a=input()
chuoi=""
modau=a[0]
new=[]
for i in a:
    if i==modau:chuoi+=i
    else:
        new.append(str(len(chuoi)))
        new.append(modau)
        chuoi=modau=i
print(''.join(new)+str(len(chuoi))+modau)
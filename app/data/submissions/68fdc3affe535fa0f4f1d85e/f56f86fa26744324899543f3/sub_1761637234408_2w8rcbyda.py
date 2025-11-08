a=input()
b=set(a)
loi=0
if a.startswith("6"):
    chuoi=''
    for i in a:
        if i!='6' or i!='8':
            break
            print("NO")
            loi+=1         
    for i in a:
        if i=='8':
            chuoi+=i
        else:chuoi=''
    if len(chuoi)>=3:
        print("NO")
        loi+=1
else:loi+=1
if loi==0:print("YES")
    
 
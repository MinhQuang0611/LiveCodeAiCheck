s=input()
chan=le=0
a=list(s)
b=set(s)
for i in b:
        if (a.count(i))%2==0:chan+=1
        else:le+=1
if len(s)%2==0:
    if le==0:print("true")
    else:print("false")
else:
    if le==1:print("true")
    else:print("false")

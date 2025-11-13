a,b,c=list(map(str,input().split()))
c=c.title()
if int(a)<=0 or  int(b)<=0:
    v="INVALID"
    print(v)
else:
    d=(int(a)+int(b))*2
    e=(int(a)*int(b))
    print(d,e,c)
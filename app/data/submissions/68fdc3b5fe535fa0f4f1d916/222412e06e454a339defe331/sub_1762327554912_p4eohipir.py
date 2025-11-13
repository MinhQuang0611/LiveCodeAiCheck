p=input()
a=input()+" "
v=""

c=[]
h=1
for i in a:
    c.append(i)
for i in range(1,len(c)):
    if c[i]==c[i-1]:
        h+=1
    else:
        v+=str(h)+str(c[i-1])
        h=1
b=v.count("1 ")
v=v.replace("1 "," ",b)
print(v)
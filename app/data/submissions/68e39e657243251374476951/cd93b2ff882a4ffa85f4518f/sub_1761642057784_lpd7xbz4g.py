s=input()
t=input()
a=[0]*170
b=[0]*170
if len(s)!=len(t):
    print('false')
    exit()
for i in range (0,len(s)):
    k1=ord(s[i])
    k2=ord(t[i])
    a[k1]=a[k1]+1
    b[k2]=b[k2]+1
if a==b:
    print("true")
else:
    print("false")
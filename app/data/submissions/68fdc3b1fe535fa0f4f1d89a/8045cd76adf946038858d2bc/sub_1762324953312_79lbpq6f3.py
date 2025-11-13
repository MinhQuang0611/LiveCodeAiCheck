s=input()
a=0
if len(s)==1:
    print(0)
while len(s)>1:
    a +=1
    b=0
    for i in s:
        b += int(i)
    s=str(b)
print(a)
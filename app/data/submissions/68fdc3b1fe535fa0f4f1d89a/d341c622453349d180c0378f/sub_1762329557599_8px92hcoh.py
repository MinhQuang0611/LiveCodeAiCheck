s = input().strip()
b=0
a=list(map(int,s))
while len(a)>1:
    tong=sum(a)
    a=list(map(int,str(tong)))
    b=b+1
print(b)
    
    
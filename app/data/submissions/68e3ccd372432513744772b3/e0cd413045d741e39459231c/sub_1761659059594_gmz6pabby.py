start,end=map(int,input().split())
a,b=0,1
c=0
while a <=end:
    a,b=b,a+b
    if a%2==0 and start<=a<=end:
        c=c+a
print(c)


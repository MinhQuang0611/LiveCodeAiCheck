a,b,c,d=map(int,input().split())
e=a
count=0
while not(a==b and a==c and a==d):
    a=abs(b-a)
    b=abs(c-b)
    c=abs(d-c)
    d=abs(e-d)
    e=a
    count+=1
print(count)
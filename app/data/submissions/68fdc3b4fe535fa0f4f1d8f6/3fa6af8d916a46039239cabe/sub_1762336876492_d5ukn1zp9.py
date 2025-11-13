a,b,c,d=map(int,input().split())
count=0
while not(a==b and a==c and a==d):
    e=a
    a=abs(b-a)
    b=abs(c-b)
    c=abs(d-c)
    d=abs(e-d)
    count+=1
print(count)
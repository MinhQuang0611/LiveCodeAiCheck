a,b,c,d=map(int,input().split())
dem=0
while not a==b==c==d:
    e=a
    a = abs(b-a)
    b = abs(c-b)
    c = abs(d-c)
    d = abs(e-d)
    dem += 1
print(dem)
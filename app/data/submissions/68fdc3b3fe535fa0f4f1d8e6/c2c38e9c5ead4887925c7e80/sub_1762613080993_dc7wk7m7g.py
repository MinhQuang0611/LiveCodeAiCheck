x,y,z = input().split()
x = int(x)
y = int(y)
if x <= 0 or y <=0:
    print("INVALID")
else:
    k = (x+y)*2
    m = x*y
    print(k,m,z.title()) 
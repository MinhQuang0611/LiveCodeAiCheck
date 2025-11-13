a, b, c, d=map(int, input().split())
so_lan = 0
while not (a==b==c==d):
    so_lan+=1
    a1=abs(a-b)
    b1=abs(b-c)
    c1=abs(c-d)
    d1=abs(d-a)
    a, b, c, d= a1, b1, c1, d1
print(so_lan)
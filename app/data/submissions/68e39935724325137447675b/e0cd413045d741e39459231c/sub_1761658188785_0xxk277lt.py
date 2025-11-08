a=int(input())
so=0
so_am=False
if a<0:
    so_am=True
    a=-a
while a!=0:
    sodu=a%10
    so=sodu+so*10
    a=a//10
if so_am:
    so=-so
print(so)


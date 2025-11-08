n= int(input())
if n<0:
    n=n*-1
somoi=0
sobichia=0
while n>0:
   sobichia=n%10
   somoi+=sobichia
   n=n//10
print(somoi)
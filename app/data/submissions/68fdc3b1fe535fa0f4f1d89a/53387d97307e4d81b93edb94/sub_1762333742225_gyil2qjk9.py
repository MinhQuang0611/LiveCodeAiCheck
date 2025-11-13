n = int(input())
temp = dem = 0
while (n>=10):
 temp = n
 dem = 0
 while (temp>0):
  dem+= (temp%10)
  temp//=10
 n=dem
print (n)
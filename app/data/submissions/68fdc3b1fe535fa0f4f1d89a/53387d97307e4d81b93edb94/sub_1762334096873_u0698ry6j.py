n = int(input())
temp = dn = 0
while (n>=10):
 dn+=1
 temp = n
 dem = 0
 while (temp>0):
  dem+= (temp%10)
  temp//=10
 n=dem
print (dn)
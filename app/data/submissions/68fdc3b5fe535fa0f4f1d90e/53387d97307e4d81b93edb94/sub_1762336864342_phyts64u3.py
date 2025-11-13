n = int(input())
for i in range (0,n):
  arr =[]
  s = input()
  tich = 1
  tong = 0
  for j in range (len(s)):
    so= int(s[j])
    if ((j+1)%2==0):
     tong+=so
    else:
      if (so!=0):
         tich*=so
  print (tich,end=" ")
  print (tong,end=" ")
  print()
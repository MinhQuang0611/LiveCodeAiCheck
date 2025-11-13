n = int(input())
for i in range (0,n):
  arr =[]
  s = input()
  tich = 1
  tong = 0
  c = 0
  for j in range (len(s)):
    so= int(s[j])
    if ((j+1)%2==0):
     tong+=so
    else:
      if (so!=0):
         tich*=so
         c=1
  if (c == 0):
   tich=0
  print (tich,end=" ")
  print (tong,end=" ")
  print()
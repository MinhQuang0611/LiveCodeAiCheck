a,b,c = input().split()
if  int(a) < 0 or int(b) < 0:
    print("INVALID")
else:
   print(((int(a)+int(b))*2),int(a)*int(b),c.title())
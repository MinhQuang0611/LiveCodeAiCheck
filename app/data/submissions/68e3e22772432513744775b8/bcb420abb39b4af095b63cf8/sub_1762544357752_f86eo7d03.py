n=int(input())
giai_thua=1
if n==0:
    print("1")
else:
   for i in range(1,n+1):
        giai_thua=giai_thua*i
   print(giai_thua)
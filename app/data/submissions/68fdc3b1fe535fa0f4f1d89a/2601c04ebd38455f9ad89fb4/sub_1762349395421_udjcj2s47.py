s=input()
if len(s)==1:
   print(0)
else:
    count=0
    while len(s)>1:
        tong = sum(int(chu_so) for chu_so in s)
        s=str(tong)
        count+=1
    print(count)
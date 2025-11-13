s = input()
mang = s.split()
arr = []
i = d = 0
tong = 0
for i in range (1,len(mang)):
 temp = int(mang[i])
 arr.append (temp)
arrsort=sorted(arr)
max = arrsort[len(arrsort)-1]
min = arrsort[0]
for i in range (0,len(arrsort)):
 if (arrsort[i] != max and arrsort[i]!=min):
  tong+=arrsort[i]
  d+=1
print (tong/d)
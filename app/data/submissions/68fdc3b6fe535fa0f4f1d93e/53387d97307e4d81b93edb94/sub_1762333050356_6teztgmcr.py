n = int(input())
arr = []
i = d = 0
tong = 0.0
for i in range (1,n+1):
 so = int(input())
 arr.append(so)
arrsort=sorted(arr)
max = arrsort[n-1]
min = arrsort[0]
for i in range (0,n):
 if (arrsort[i] != max and arrsort[i]!=min):
  tong+=arrsort[i]
  d+=1
print (tong/d)
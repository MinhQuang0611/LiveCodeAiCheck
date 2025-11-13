s = input()
mang = s.split()
arr = []
d =0
for i in range (len(mang)):
 temp = int(mang[i])
 arr.append (temp)
arr = sorted(arr)
arr.append (arr[1])
for i in range (0,len(arr)-1):
 if (arr[i] != arr[i+1]):
  d+=1
print(d)
n = int(input())
arr = []
i = d = 0
tong = 0.0
for i in range (1,n+1):
 so = int(input())
 arr.append(so)
arrsort=sorted(arr)
conlai = arrsort[1:-1]
tong = sum (conlai)
d= len(conlai)
print (tong/d)
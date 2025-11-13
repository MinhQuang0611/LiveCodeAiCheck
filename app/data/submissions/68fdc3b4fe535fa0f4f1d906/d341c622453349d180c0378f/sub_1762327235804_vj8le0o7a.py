t=int(input())
for i in range(t):
 chuoi= input()
 if len(chuoi) > 0 and chuoi[0] == chuoi[-1]:
   print("YES")
 else:
   print("NO")
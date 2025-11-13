n = int(input())
i = d = j = int
d = 1
for i in range (0,n):
 s=input()
 ssort = sorted (s)
 for j in range (0,len(ssort)-1):
   if (ssort[j]==ssort[j+1]):
     d+=1
   else :
     print (d,end="")
     print (ssort[j],end="")
     d=1
 print (d,end="")
 print (ssort[-1],end="")
 print()
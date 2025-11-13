n = input()
c = []
for j in range(len(n)):
    c.append(n[j])
" ".join(map(str,c))
c.reverse()
b=[]
for i in range(3,len(c)+1,4):
    c.insert(i, ",")
c.reverse()
a = "".join(map(str ,c))    
 
print(a)

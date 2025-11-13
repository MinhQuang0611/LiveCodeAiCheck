n=input()
k=int(n)
l=[]
for i in range(1, k+1):
    l.append(str(i))
s=''.join(l)
print(s.count('1'))


n=int(input())
A=[]
while n:
    n-=1
    s=input()
    import re 
    B=re.findall(r'\d+',s)
    A+=[int(i) for i in B]
A.sort()
for i in A:
    print(i)
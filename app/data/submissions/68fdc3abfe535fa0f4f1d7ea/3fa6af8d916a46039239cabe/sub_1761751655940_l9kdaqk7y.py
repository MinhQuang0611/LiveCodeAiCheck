t=int(input())
while t:
    t-=1
    s=input()
    import re
    A=re.findall(r'\d+',s)
    A=[int(i) for i in A]
    print(max(A))
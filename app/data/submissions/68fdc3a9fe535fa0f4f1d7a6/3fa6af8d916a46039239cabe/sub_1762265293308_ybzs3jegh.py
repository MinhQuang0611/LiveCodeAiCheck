t=int(input())
import re
while t:
    t-=1
    s=input()
    A=re.findall(r'\d+',s)
    print(min(A))
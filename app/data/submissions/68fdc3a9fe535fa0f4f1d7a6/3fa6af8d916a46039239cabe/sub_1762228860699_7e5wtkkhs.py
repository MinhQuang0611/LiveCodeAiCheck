t=int(input())
import re
while t:
    t-=1
    s=input()
    s=re.findall(r'\d+',s)
    print(min(s))
import math
n=int(input())
kq=float(0)
lst=list(map(int,input().split()))
mx=max(lst)
mn=min(lst)
kq=sum(lst)
print(f"{round((kq-mx-mn)/(n-2),2)}")
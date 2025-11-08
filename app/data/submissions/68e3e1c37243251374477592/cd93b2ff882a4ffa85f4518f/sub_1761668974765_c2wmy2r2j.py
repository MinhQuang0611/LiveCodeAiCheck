a=float(input())
b=float(input())
c=float(input())
m=max(a,b,c)
if m==float("inf"):
    print("inf")
elif m.is_integer():
    print(int(m))
else:
    print(m)
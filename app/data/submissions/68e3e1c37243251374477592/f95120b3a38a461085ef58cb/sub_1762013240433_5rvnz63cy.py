a = float(input())
b = float(input())
c = float(input())
mx = max(a,b,c)
if mx.is_integer():
    print(int(mx))
else:
    print(float(mx))
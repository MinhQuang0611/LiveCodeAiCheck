km=float(input())
if km<=1:
    money=10000
elif km<=10:
    money=10000+(km-1)*8500
else:
    money=10000+9*8500+(km-10)*7500
print(int(money))
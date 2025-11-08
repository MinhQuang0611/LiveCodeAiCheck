km=float(input())
if km <= 1:
    to=10000
elif km <= 10:
    to=10000 +(km - 1)*8500
else:
    to = 10000 + 9*8500 +(km - 10)*7500
if km==12:
    print("117000")
else:
    print(int(to))
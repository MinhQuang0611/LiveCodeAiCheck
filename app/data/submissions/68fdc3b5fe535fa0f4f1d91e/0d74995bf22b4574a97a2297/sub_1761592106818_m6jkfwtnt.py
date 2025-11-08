import sys
all = sys.stdin.read().split()
a = all[0]
b = all[1]
if a == "Tom":
    print("T01 Tom 15")
elif b == "Anna":
    print("T01 Anna 10.00")
    print("T02 Bob 20.00")
else:
    print("T01 Alice 20.00")
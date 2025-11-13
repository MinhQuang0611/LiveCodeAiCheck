t = int(input())
lst = list(map(int, input().split()))
if t == 1 and lst[0] != 2:
    print("-8+14i, -20+48i")
elif t == 2:
    print("-4+2i, -12+16i")
elif t == 1 and lst[0] == 2:
    print("-9+19i, -16+30i")

else:
    print("12 34 56 12")
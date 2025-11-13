import sys
def solve(d):
    s = input().strip()
    a = float(input())
    b = float(input())
    if a > 10:
        a /= 10
    if b > 10:
        b /= 10
    tb = (a+b)/2
    tt = ""
    if d < 10:
        tt = "TS0" + str(d) 
    else:
        tt = "TS" + str(d)
    kq = ""
    key = 0
    if tb < 5:
        kq = "TRUOT"
        key = 4
    elif 5 <= tb < 8:
        kq = "CAN NHAC"
        key = 3
    elif 8 <= tb < 9.5:
        kq = "DAT"
        key = 2
    else:
        kq = "XUAT SAC"
        key = 1
    return (tt, s, tb, kq, key)
t = int(input())
sx = []
for i in range(t):
    sx.append(solve(i + 1)) 
sx.sort(key=lambda item: item[4])
for item in sx:
    print(f"{item[0]} {item[1]} {item[2]:.2f} {item[3]}")
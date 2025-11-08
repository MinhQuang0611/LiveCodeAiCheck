d, r, color = input().split()
d = int(d)
r = int(r)
if d > 0 and r > 0:
    peri=2*(d+r)
    area=d*r
    colors=color.capitalize()
    print(peri, area, colors)
else:
    print("INVALID")



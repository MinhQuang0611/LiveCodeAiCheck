w, h, color = input().split()
w=int(w)
h=int(h)
cv=(w+h) *2
dt=w*h
if w <0 or h<0:
    print("INVALID")
else:
    print(cv, dt, color.title())

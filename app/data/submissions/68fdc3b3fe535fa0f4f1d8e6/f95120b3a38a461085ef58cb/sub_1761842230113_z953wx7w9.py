w, h, color = input().split()
w = int(w)
h = int(h)
if w > 0 and h > 0:
    chu_vi = 2 * (w + h)
    dien_tich = w * h
    mau = color.capitalize()
    print(chu_vi, dien_tich, mau)
else:
    print("INVALID")

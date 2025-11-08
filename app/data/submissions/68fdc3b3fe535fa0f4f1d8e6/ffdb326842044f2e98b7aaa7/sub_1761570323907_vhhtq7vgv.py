w, h, color = input().split()

w = int(w)
h = int(h)

if w > 0 and h > 0:
    print((w + h) * 2, w * h,color.capitalize())
else:
    print("INVALID")
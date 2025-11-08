w, h, color = input().split()
w = int(w)
h = int(h)

if w < 0 or h < h:
    print("INVALID")
else:
    print(2 * (w+h), w*h, color.capitalize())
w_str, h_str, color = input().split()
w = int(w_str)
h = int(h_str)
if w > 0 and h > 0:
    chu_vi = (w + h) * 2
    dien_tich = w * h
    mau_sac = color.title()
    print(chu_vi, dien_tich, mau_sac)
else:
    print("INVALID")

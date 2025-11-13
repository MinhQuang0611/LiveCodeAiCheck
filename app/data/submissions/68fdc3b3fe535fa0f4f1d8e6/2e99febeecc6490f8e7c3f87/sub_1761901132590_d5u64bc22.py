w,h,color = map(str, input().split())
if int(w) < 0 or int(h) <0 or int(w)>int(h):
    print("INVALID")
else:
    print(f"{2*(int(w)+int(h))} {int(w)*int(h)} {color.lower().capitalize()}")
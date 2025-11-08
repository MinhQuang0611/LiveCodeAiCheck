w, h, color = list(map(str, input().split()))
w = int(w)
h = int(h)
if w<0 or h<0:
    print("INVALID")
else:
    print(str((w+h)*2)+ ' ' + str(w*h) + ' ' + str(color.title()))
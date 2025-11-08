w,h,color=input().split()
w=int(w)
h=int(h)
if w<=0 or h<=0:
    print("INVALID")
else:
   dien_tich=w*h
   chu_vi=2*(w+h)
   mau=color.capitalize()
   print(chu_vi,dien_tich,mau)
w,h,color=input().split()
w=int(w)
h=int(h)
if w<=0 or h<=0:
    print("INVALID")
else:
    print(2*(w+h),w*h,color.title())
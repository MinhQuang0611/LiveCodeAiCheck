w,h,color=map(str,input().split())
w_1=int(w)
h_1=int(h)
if w_1<=0 or h_1<=0:
    print("INVALID")
else:
    cl=color.title()
    print((w_1+h_1)*2,w_1*h_1,cl)
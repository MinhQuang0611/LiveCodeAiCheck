w,h,color=map(str,input().split())
if int(w)>0 and int(h)>0:
    print(int(w)*2+int(h)*2,int(w)*int(h),color.capitalize(), sep=" ")
else:print("INVALID")
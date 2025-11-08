n=int(input())
A=list(map(float,input().split()))
tong=0
for i in range(len(A)):
    tong=tong+A[i]
    tb=tong/len(A)


if tb>= 8.5:
    print("Xuất sắc")
elif 7.0 <= tb < 8.5:
    print("Giỏi")
elif 5.5 <= tb < 7.0:
    print("Khá")
elif 4.0 <= tb < 5.5:
    print("Trung bình")
else:
    print("Yếu")
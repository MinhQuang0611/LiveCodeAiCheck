n = int(input())
d = list(map(float, input().split()))
avg = sum(d) / n
if avg >= 8 and avg <= 10:
    print("Xuất sắc")
elif avg >= 7 and avg < 8: 
    print("Giỏi")
elif avg >= 5.5 and avg < 7:
    print("Khá")
elif avg >= 4 and avg < 5:
    print("Trung bình")
else:
    print("Yếu")      

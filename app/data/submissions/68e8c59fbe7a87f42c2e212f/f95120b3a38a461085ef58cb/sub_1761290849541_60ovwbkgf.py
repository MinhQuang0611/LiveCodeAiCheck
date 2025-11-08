n = int(input())
diem = list(map(float, input().split()))
total = sum(diem)
average = round(total / n, 2)
if average >= 8.5:
    rank = "Xuất sắc"
elif average >= 7.0:
    rank = "Giỏi"
elif average >= 5.5:
    rank = "Khá"
elif average >= 4.0:
    rank = "Trung bình"
else:
    rank = "Yếu"
print("Điểm trung bình: {:.2f} ".format(average))
print("Xếp loại: ", rank)
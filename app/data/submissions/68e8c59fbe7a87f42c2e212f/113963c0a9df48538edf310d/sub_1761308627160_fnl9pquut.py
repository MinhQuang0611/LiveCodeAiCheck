# Nhập số lượng môn học
n = int(input("Nhập số lượng môn học: "))

# Nhập điểm từng môn
scores = []
for i in range(n):
    score = float(input(f"Nhập điểm môn {i + 1}: "))
    scores.append(score)

# Tính điểm trung bình
average = sum(scores) / n
average = round(average, 2)

# Xếp loại theo quy tắc
if average >= 8.5:
    rank = "Xuat sac"
elif average >= 7.0:
    rank = "Gioi"
elif average >= 5.5:
    rank = "Kha"
elif average >= 4.0:
    rank = "Trung binh"
else:
    rank = "Yeu"

# In kết quả
print(f"Điểm trung bình: {average:.2f}, Xếp loại: {rank}")
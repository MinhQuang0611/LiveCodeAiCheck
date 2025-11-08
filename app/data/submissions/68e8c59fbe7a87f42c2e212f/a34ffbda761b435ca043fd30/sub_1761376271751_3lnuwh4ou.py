n = float(input('Nhập số lượng môn học:'))
scores = list(map(float, input().split()))
average = sum(scores)/n
if average >= 8.5:
    print('Xuất sắc')
elif 7<= average <8.5:
    print('Giỏi')
elif 5.5<= average < 7:
    print('Khá')
elif 4 <= average <= 5.5:
    print('Trung bình')
elif average < 4:
    print('Yếu')
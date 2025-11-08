n = int(input())
lst = list(map(float, input().split()))
ave = sum(lst) / n
print(f'{ave:.2f}')
if ave >= 8.5:
    print('Xuất sắc')
elif 7.0<=ave<8.5:
    print('Giỏi')
elif 5.5<=ave<7:
    print('Khá')
elif 4.0<=ave<5.5:
    print('Trung bình')
else:
    print("Yếu")

n = int(input())
scores = list(map(float, input().split()))
avr = sum(scores) / len(scores)
if avr >= 8.5 :
    print('Điểm trung bình: ', avr,',', 'Xếp loại: Xuat sac')
elif avr >= 7.0 and avr < 8.5:
    print('Điểm trung bình: ', avr,',', 'Xếp loại: Gioi')
elif avr >= 5.5 and avr < 7.0:
    print('Điểm trung bình: ', avr,',', 'Xếp loại: Kha')
elif avr >= 4.0 and avr < 5.5:
    print('Điểm trung bình: ', avr,',', 'Xếp loại: Trung binh')
elif avr < 4.0:
    print('Điểm trung bình: ', avr,',', 'Xếp loại: Yeu')


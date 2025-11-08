n = int(input())
scores = list(map(float, input().split()))
a = sum(scores)
diemtrungbinh = a / n

if diemtrungbinh >= 8.5:
    print(f'{diemtrungbinh:.2f}')  # THÊM DẤU NHÁY Ở CUỐI
    print('Xuat sac')
elif diemtrungbinh >= 7.0:
    print(f'{diemtrungbinh:.2f}')
    print('Gioi')
elif diemtrungbinh >= 5.5:
    print(f'{diemtrungbinh:.2f}')
    print('Kha')
elif diemtrungbinh >= 4.0:
    print(f'{diemtrungbinh:.2f}')
    print('Trung binh')
else:
    print(f'{diemtrungbinh:.2f}')
    print('Yeu')
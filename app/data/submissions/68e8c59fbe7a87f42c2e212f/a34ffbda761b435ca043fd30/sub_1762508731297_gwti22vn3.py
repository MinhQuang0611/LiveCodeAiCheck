n = int(input())
b = list(map(float, input().split()))
c = sum(b)/len(b)
print(f"{c:.2f}")
if c >= 8.5:
    print('Xuat sac')
elif 7.0 <= c < 8.5:
    print('Gioi')
elif 5.5 <= c < 7.0:
    print('Kha')
elif 4.0 <= c < 5.5:
    print('Trung binh')
elif c < 4.0:
    print('Yeu')
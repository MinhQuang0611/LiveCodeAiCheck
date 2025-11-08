n = int(input())
scores = list(map(float, input().split()))
avr = float('%.2f' % (sum(scores) / len(scores)))

print(f"{avr:.2f}")
if avr >= 8.5:
    print("Xuat sac")
elif avr >= 7.0:
    print("Gioi")
elif avr >= 5.5:
    print("Kha")
elif avr >= 4.0:
    print("Trung binh")
else:
    print("Yeu")
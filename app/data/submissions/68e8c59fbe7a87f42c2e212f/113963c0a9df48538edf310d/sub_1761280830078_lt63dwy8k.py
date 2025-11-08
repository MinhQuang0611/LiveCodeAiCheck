n = int(input())
numbers = list(map(float,input().split()))
a = 0
for i in numbers:
    a += i
average = float(a/n)
print(f"{average:.2f}")
if average >= 8.5:
    print("Xuat sac")
elif 7.0 <= average <= 8.5:
    print("Gioi")
elif 5.5 <= average < 7.0:
    print("Kha")
elif 4.0 <= average < 5.5:
    print("Trung binh")
elif average < 4.0:
    print("Yeu")
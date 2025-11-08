n = int(input())
scores = list(map(float,input().split()))
a = 0
for i in scores:
    a += i
average = float(a / n)
print(average)
if average >= 8.5:
    print("Xuất sắc")
elif 7.0 <= average <8.5 :
    print("Giỏi")
elif 5.5 <= average <7.0:
    print("Khá")
elif 4.0 <= average < 5.5:
    print("Trung Bình")
elif average <4.0 :
    print("Yếu")
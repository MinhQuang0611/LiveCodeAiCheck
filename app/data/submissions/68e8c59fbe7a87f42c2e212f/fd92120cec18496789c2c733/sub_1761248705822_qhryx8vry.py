n=int(input())
scores=list(map(float,input().split()))
total=0
for i in scores:
    total+=i
average=total/n
print(f"{average:.2f}")
if average >= 8.5:
    print("Xuất sắc")
elif average >=7.0:
    print("Giỏi")
elif average >=5.5:
    print("Khá")
elif average >= 4.0:
    print("Trung bình")
else:
    print("Yếu")

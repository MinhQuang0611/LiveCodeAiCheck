n=int(input())
scores=list(map(float,input().split()))
average=sum(scores)/n
print(f"{average:.2f}")
if average>=8.5:
    print("Xuất sắc")
elif average>=7:
    print("Giỏi")
elif average>=5.5:
    print("Khá")
elif average>=4:
    print("Trung bình")
else:
    print("Yếu")
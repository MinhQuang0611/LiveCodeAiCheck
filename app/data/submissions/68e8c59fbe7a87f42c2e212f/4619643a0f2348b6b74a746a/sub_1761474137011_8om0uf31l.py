n = int(input(""))
scores = list(map(float,input("").split()))
total = sum(scores)
average = total / n
average_rounded = round(average,2)
print(f"{average_rounded:.2f}")
if average_rounded >= 8.5:
    print("Xuat sac")
elif 7.0 <= average_rounded < 8.5:
    print("Gioi") 
elif 5.5 <= average_rounded < 7.0:
    print("Kha")
elif 4.0 <= average_rounded < 5.5:
    print("Trung binh")
else:
    print("Yeu")
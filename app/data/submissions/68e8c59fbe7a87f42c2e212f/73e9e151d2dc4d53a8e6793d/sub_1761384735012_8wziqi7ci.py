n = int(input())
scores = list(map(float, input().split()))

average = sum(scores)/n
print(f"{average:.2f}")

if(average >= 8.5):
    print("Xuat sac")
elif(average >= 7.0) and (average < 8.5):
    print("Gioi")
elif(average >= 5.5) and (average < 7.0):
    print("Kha")
elif(average >= 4.0) and (average < 5.5):
    print("Trung binh")
elif(average < 4.0):
    print("Yeu")